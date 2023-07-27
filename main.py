import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import ast
import operator as op
from sympy import symbols
class MathParser:
    """ Basic parser with local variable and math functions

    Args:
       vars (mapping): mapping object where obj[name] -> numerical value
       math (bool, optional): if True (default) all math function are added in the same name space

    Example:

       data = {'r': 3.4, 'theta': 3.141592653589793}
       parser = MathParser(data)
       assert parser.parse('r*cos(theta)') == -3.4
       data['theta'] =0.0
       assert parser.parse('r*cos(theta)') == 3.4
    """

    _operators2method = {
        ast.Add: op.add,
        ast.Sub: op.sub,
        ast.BitXor: op.xor,
        ast.Or:  op.or_,
        ast.And: op.and_,
        ast.Mod:  op.mod,
        ast.Mult: op.mul,
        ast.Div:  op.truediv,
        ast.Pow:  op.pow,
        ast.FloorDiv: op.floordiv,
        ast.USub: op.neg,
        ast.UAdd: lambda a: a
    }

    def __init__(self, vars, math=True):
        self._vars = vars
        if not math:
            self._alt_name = self._no_alt_name

    def _Name(self, name):
        try:
            return self._vars[name]
        except KeyError:
            return self._alt_name(name)

    @staticmethod
    def _alt_name(name):
        if name.startswith("_"):
            raise NameError(f"{name!r}")
        try:
            return getattr(math, name)
        except AttributeError:
            raise NameError(f"{name!r}")

    @staticmethod
    def _no_alt_name(name):
        raise NameError(f"{name!r}")

    def eval_(self, node):
        if isinstance(node, ast.Expression):
            return self.eval_(node.body)
        if isinstance(node, ast.Num):  # <number>
            return node.n
        if isinstance(node, ast.Name):
            return self._Name(node.id)
        if isinstance(node, ast.BinOp):
            method = self._operators2method[type(node.op)]
            return method(self.eval_(node.left), self.eval_(node.right))
        if isinstance(node, ast.UnaryOp):
            method = self._operators2method[type(node.op)]
            return method(self.eval_(node.operand))
        if isinstance(node, ast.Attribute):
            return getattr(self.eval_(node.value), node.attr)

        if isinstance(node, ast.Call):
            return self.eval_(node.func)(
                *(self.eval_(a) for a in node.args),
                **{k.arg: self.eval_(k.value) for k in node.keywords}
            )
            return self.Call(self.eval_(node.func), tuple(self.eval_(a) for a in node.args))
        else:
            raise TypeError(node)

    def parse(self, expr):
        return self.eval_(ast.parse(expr, mode='eval'))
data = {
    'ln': lambda x, ln=np.log: ln(x),
    'sin': lambda x, sin=np.sin: sin(x),
    'arcsin': lambda x, arcsin=np.arcsin: arcsin(x),
}
parser = MathParser(data)
def calc_function(function:str, params:dict):
    param_keys = params.keys()
    for key in param_keys:
        data[key] = params[key]
    return parser.parse(function.replace('^', '**'))
# def f(x, a, b):
#     return calc_function('a + b*x', x, {'a' : a, 'b': b})
def create_dict(list1, list2):
    dict_ = {}
    for i, item in enumerate(list1):
        dict_[item] = list2[i]
    return dict_
def return_f(func, params):
    return lambda *args: calc_function(func, create_dict(params, args))
def create_initial_value_array(params):
    returned = []
    for i in range(len(params) - 1):
        returned.append(0)
    return returned
def create_format_of_results(params):
    result = 'fit: '
    for i in range(1, len(params)):
        result += f'{params[i]}=%.2E, '
    return result
func = 'a*ln(x) + b'
params = list('xab')
xdata = [10.30, 10.30, 10.10, 9.30, 8.40, 7.30, 8.40, 7.90, 7.60, 7.60, 6.90, 7.40, 8.10, 7.00, 6.50, 5.80]
ydata = [183.800 ,183.200 ,174.900 ,173.500 ,172.900 ,173.200 ,173.200 ,169.700 ,174.500 ,177.900 ,188.100 ,203.200 ,230.200 ,258.200 ,309.800 ,329.800]
f = return_f(func, params)
if len(xdata) != len(ydata):
    raise ValueError("Data wrong")
length = len(xdata)

popt, pcov = curve_fit(f, xdata, ydata, create_initial_value_array(params))
print(popt)
ydatanew = []
for i in range(length):
    ydatanew.append(f(xdata[i], *popt))
residuals = []
for i in range(length):
    residuals.append(ydata[i] - ydatanew[i])
ss_res = np.sum(np.square(residuals))
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

print(r_squared)

plt.plot(xdata, ydata, 'b.', label='data')
plt.plot(xdata, ydatanew, 'r-',
         label=create_format_of_results(params) % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()