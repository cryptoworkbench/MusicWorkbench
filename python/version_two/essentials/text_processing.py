def underscore(text):
    return text.replace(' ', '_')

def prepare_varname(text):
    return underscore(text.replace('#', '_sharp').lower())
