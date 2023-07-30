import re
import numpy as np
import math
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