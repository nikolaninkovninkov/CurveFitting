from ..mathparser.MathParser import MathParser, get_params, get_data
from . import utils
import math
import numpy as np
from scipy.optimize import curve_fit
import re
def return_f(func, params_letters):
    def f(*args):
        data_copy = get_data()
        for i, param_letter in enumerate(params_letters):
            data_copy[param_letter] = args[i]
        parser = MathParser(data_copy)
        return parser.parse(func) 
    return f
import math
import re

    
def fit_curve(xdata, ydata, func, to_print=False):
    clean_func = utils.clean_input_function(func)
    params = ['x', *get_params(clean_func)]
    f = return_f(clean_func, params)
    new_initial_values = [1 for _ in params[1:]]
    if len(xdata) != len(ydata):
        raise ValueError("Data wrong")
    popt, pcov = curve_fit(f, xdata, ydata, new_initial_values)
    r_squared =  utils.calc_r_squared(xdata, ydata, popt, f)
    perr = np.sqrt(np.diag(pcov))
    if to_print:
        for i in range(1, len(params)):
            print(f'{params[i]}:{popt[i-1]}±{perr[i-1]}')
        print(f'R\N{SUPERSCRIPT TWO}: {r_squared}')
    return [popt, perr, r_squared, params]
