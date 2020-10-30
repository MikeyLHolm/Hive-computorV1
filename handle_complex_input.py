def handle_zero_degree_form(left_list, right_list):
    left_form_handled = [obj + '*X0' if not 'X' in obj.upper() else obj for obj in left_list]
    right_form_handled = [obj + '*X0' if not 'X' in obj.upper() else obj for obj in right_list]
    return left_form_handled, right_form_handled


def handle_no_coeff(left_list, right_list):
    for i, obj in enumerate(left_list):
        if obj[0] == '-':
            if obj[1:].upper() == 'X':
                left_list[i] = '-1*X'
        else:
            if obj.upper() == 'X':
                left_list[i] = '1*' + obj

    for i, obj in enumerate(right_list):
        if obj[0] == '-':
            if obj[1:].upper() == 'X':
                right_list[i] = '-1*X'
        else:
            if obj.upper() == 'X':
                right_list[i] = '1*' + obj

    return left_list, right_list


def handle_no_degree(left_list, right_list):
    left_no_degree_handled = [obj + '1' if obj[-1].upper() == 'X' else obj for obj in left_list]
    right_no_degree_handled = [obj + '1' if obj[-1].upper() == 'X' else obj for obj in right_list]
    return left_no_degree_handled, right_no_degree_handled


def handle_complex_input(left_list, right_list):
    left_list, right_list = handle_zero_degree_form(left_list, right_list)
    left_list, right_list = handle_no_coeff(left_list, right_list)
    left_list, right_list = handle_no_degree(left_list, right_list)
    return left_list, right_list