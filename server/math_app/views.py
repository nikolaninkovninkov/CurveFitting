import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .code.curve_fitter import curve_fitter as cf, utils
from .code.newtons_method import newtons_method as nm
import ast
@csrf_exempt
def fit_curve(request):
    if request.method != 'POST':
        response_data = {
            'error': 'Invalid request method. Only POST requests are allowed.'
        }
        return JsonResponse(response_data, status=405)  # 405: Method Not Allowed
    data = json.loads(request.body)
    try:
        xdata = data['xdata']
        ydata = data['ydata']
        func = data['function']
        popt, perr, r_squared, params = cf.fit_curve(xdata, ydata, func, False)
        response_data: dict[str, str] = {}
        for i in range(1, len(params)):
            response_data[params[i]] = {
                'value' : popt[i-1],
                'var' : perr[i-1]
            }
        response_data['r_squared'] = r_squared
        replaced_function = utils.clean_output_function(utils.replace_params_with_numerical_value(func, utils.create_dict_from_lists(params[1:], popt), data))
        response_data['output_function'] = replaced_function
        return JsonResponse(response_data)
    except:
        response_data = {
            'error': 'Invalid data.'
        }
        return JsonResponse(response_data, status=400)
@csrf_exempt
def newtons_method(request):
    if request.method != 'POST':
        response_data = {
            'error': 'Invalid request method. Only POST requests are allowed.'
        }
        return JsonResponse(response_data, status=405)  # 405: Method Not Allowed
    try:
        data = json.loads(request.body)
        func = data['function']
        root = nm.get_root(func)
        response_data = {}
        response_data['root'] = root
        return JsonResponse(response_data)
    except:
        response_data = {
            'error': 'Invalid data.'
        }
        return JsonResponse(response_data, status=400)    
