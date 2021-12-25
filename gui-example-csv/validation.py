
def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-NAME-']) == 0:
        values_invalid.append('Name')
        is_valid = False
    
    if len(values['-ADDRESS-']) == 0:
        values_invalid.append('Address')
        is_valid = False

    if len(values['-PHONE_NUMBER-']) == 0:
        values_invalid.append('Passport Number')
        is_valid = False

    result = {"is_valid": is_valid, "values_invalid": values_invalid}
    return result

def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return error_message