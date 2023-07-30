import numpy as np
def create_dict_from_lists(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}
def create_format_of_results(params):
    return 'fit: ' + ', '.join(f'{param}=%.4E' for param in params[1:])
def clean_function(function):
    return function.replace('^', '**')
def calc_r_squared(xdata, ydata, popt, f):
    length = len(xdata)
    ydatanew = []
    for i in range(length):
        ydatanew.append(f(xdata[i], *popt))
    residuals = []
    for i in range(length):
        residuals.append(ydata[i] - ydatanew[i])
    ss_res = np.sum(np.square(residuals))
    ss_tot = np.sum((ydata-np.mean(ydata))**2)
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared
def create_pts_for_graph(f, coeff, bounds, points=1000):
    xdata = np.linspace(bounds[0], bounds[1], points)
    ydata = []
    for i in range(points):
        ydata.append(f(xdata[i], *coeff))
    return (xdata, ydata)
def get_bounds_from_xdata(xdata):
    return (min(xdata), max(xdata))
