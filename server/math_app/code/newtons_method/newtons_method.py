import random
from .utils import clean_input_function
from sympy import parse_expr, diff
EPSILON = 1e-15
def get_root(func, start_value=random.random()):
    f = parse_expr(clean_input_function(func))
    x = parse_expr('x')
    df_dx = diff(f, x)
    iterations = 0
    current_x = start_value
    while iterations < 30 and abs(f.subs(x, current_x)-0) > EPSILON:
        current_x = current_x - f.subs(x, current_x)/df_dx.subs(x, current_x)
        iterations += 1
    return float(current_x)