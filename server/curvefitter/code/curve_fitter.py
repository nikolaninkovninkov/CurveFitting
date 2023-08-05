from .MathParser import MathParser
from . import utils
import math
import numpy as np
from scipy.optimize import curve_fit
import re
data = {
    "abs":np.abs,
    "arccos":np.arccos,  
    "arccosh":np.arccosh,
    "acoth": lambda x: 0.5*np.log((x+1)/(x-1)),    
    "arcsin":np.arcsin,  
    "arcsinh":np.arcsinh,
    "arctan":np.arctan,  
    "arctanh":np.arctanh,
    "cos":np.cos,
    "cosh":np.cosh,
    "coth": lambda x: np.cosh(x)/np.sinh(x),
    "degrees":np.degrees,
    "erf":math.erf,
    "exp":np.exp,
    "fact":math.factorial,
    "ln":np.log,
    "log": lambda x, base: np.log(x)/np.log(base),
    "log10":np.log10,
    "mod":lambda a, b: np.mod(a, b),
    "pi":np.pi,
    "pow":lambda x, power: np.pow(x, power),
    "radians":np.radians,
    "sin":np.sin,
    "sinh":np.sinh,
    "sqrt":np.sqrt,
    "tan":np.tan,
    "tanh":np.tanh
}

def return_f(func, params_letters):
    def f(*args):
        data_copy = data.copy()
        for i, param_letter in enumerate(params_letters):
            data_copy[param_letter] = args[i]
        parser = MathParser(data_copy)
        return parser.parse(func) 
    return f
def get_params(func):
    regex = re.compile('[^a-zA-Z]')
    func = regex.sub('', func)
    for reserved_word in data.keys():
        func = func.replace(reserved_word, '')
    func = func.replace('x', '')
    params = list(func)
    unique_params = []
    for param in params:
        if param not in unique_params:
            unique_params.append(param)
    return unique_params
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
def get_params(func):
    regex = re.compile('[^a-zA-Z]')
    func = regex.sub('', func)
    for reserved_word in data.keys():
        func = func.replace(reserved_word, '')
    func = func.replace('x', '')
    params = list(func)
    unique_params = []
    for param in params:
        if param not in unique_params:
            unique_params.append(param)
    return unique_params