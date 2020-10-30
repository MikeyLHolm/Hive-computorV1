def handle_zero_degree_form(left_list, right_list):
    left_form_handled = [obj + '*X0' if not 'X' in obj.upper() else obj for obj in left_list]
    right_form_handled = [obj + '*X0' if not 'X' in obj.upper() else obj for obj in right_list]
    return left_form_handled, right_form_handled


def handle_no_coeff():
    pass


def handle_no_degree():
    pass


def handle_complex_input():
#     handle_zero_degree_form()
#     handle_no_coeff() #no coeff = coeff=1
#     handle_no_degree() #no degree = degree=1
#     remove_empty_items()
    pass