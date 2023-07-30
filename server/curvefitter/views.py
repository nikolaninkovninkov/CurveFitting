import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .code import curve_fitter as cf
import ast
@csrf_exempt
def fit_curve(request):
    if request.method != 'POST':
        response_data = {
            'error': 'Invalid request method. Only POST requests are allowed.'
        }
        return JsonResponse(response_data, status=405)  # 405: Method Not Allowed
    data = json.loads(request.body)
    # try:
    xdata = data['xdata']
    ydata = data['ydata']
    func = data['function']
    print(xdata, ydata, func)
    popt, perr, r_squared, params = cf.fit_curve(xdata, ydata, func, True)
    response_data: dict[str, str] = {}
    for i in range(1, len(params)):
        response_data[params[i]] = {
            'value' : popt[i-1],
            'var' : perr[i-1]
        }
    response_data['r_squared'] = r_squared
    return JsonResponse(response_data)
    # except:
    #     response_data = {
    #         'error': 'Invalid data.'
    #     }
    #     return JsonResponse(response_data, status=400)

