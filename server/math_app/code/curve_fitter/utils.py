import numpy as np
import math
def create_dict_from_lists(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}
def clean_input_function(function):
    cleaned = function.replace(" ", "")
    cleaned = cleaned.replace('+-', '-')
    cleaned = cleaned.replace('^', '**')
    return cleaned
def clean_output_function(function):
    cleaned = function.replace(" ", "")
    cleaned = cleaned.replace('+-', '-')
    return cleaned
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
def find_all_occurrences(main_string, substring):
    occurrences = []
    start = 0
    while True:
        start = main_string.find(substring, start)
        if start == -1:
            break
        occurrences.append(start)
        start += 1
    return occurrences
def individial_occurences(occurences_dict: dict):
    occurences = []
    reserved_words = []
    n = 0
    for key in occurences_dict.keys():
        value = occurences_dict[key]
        for index in value:
            reserved_words.append(key)
            occurences.append(index)
            n+=1
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if occurences[j] > occurences[j+1]:
                occurences[j], occurences[j+1] = occurences[j+1], occurences[j]
                reserved_words[j], reserved_words[j+1] = reserved_words[j+1], reserved_words[j]
                swapped = True
        if (swapped == False):
            break
    return (reserved_words, occurences)
def split_with_reserved_words(input_string, reserved_words):
    occurences_of_reserved_words = {}
    for reserved_word in reserved_words:
        occurences_of_reserved_words[reserved_word] = find_all_occurrences(input_string, reserved_word)
    split_input_string = [_ for _ in input_string]
    individual_reserved_words, individual_occurences = (individial_occurences(occurences_of_reserved_words))
    result_list = []
    og_curr_index = 0
    for i in range(0, len(individual_reserved_words)):
        key = individual_reserved_words[i]
        value = individual_occurences[i]
        result_list.extend(split_input_string[og_curr_index:value])
        og_curr_index += value - og_curr_index
        result_list.append(key)
        og_curr_index += len(key)
    result_list.extend(split_input_string[og_curr_index:len(split_input_string)])
    return result_list
def replace_params_with_numerical_value(func, params, data):
    split = split_with_reserved_words(func, data.keys())
    for index, el in enumerate(split):
        if el in params.keys():
            split[index] = format_number(params[el])
    return ''.join(split)
def format_number(number):
    def gen_10_multiplier(b):
        return_str = ''
        if b > 0:
            return_str = '1'
            for i in range(b):
                return_str += '0'
        if b < 0:
            return_str = '0.'
            for i in range(abs(b)-1):
                return_str += '0'
            return_str += '1'
        return return_str
    if 'e' not in str(number):
        return str(number)
    a, b = str(number).split('e')
    a = float(a)
    b = int(b)
    if b == 0:
        return str(a)
    return str(a)+'*'+str(gen_10_multiplier(b))