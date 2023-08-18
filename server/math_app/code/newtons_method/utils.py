def clean_input_function(function):
    cleaned = function.replace(" ", "")
    cleaned = cleaned.replace('+-', '-')
    cleaned = cleaned.replace('^', '**')
    return cleaned