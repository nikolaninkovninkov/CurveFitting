import math
import ast
import operator as op
import numpy as np
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
    "log":np.log,
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
def get_data():
    return data.copy()
