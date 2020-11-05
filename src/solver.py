from src.degree import handle_degree, sort_get_degree
from src.handle_complex_input import handle_complex_input
from src.int_or_float import handle_int_or_float
from src.object_related import get_list_of_objects, clean_object_list
from src.plotting import plot
from src.read_and_parse import parse_input, read_input, remove_empty_items
from src.reduced_form import reduced_form
from src.solve_equation import solve_equation


def solve():
    data, to_plot = read_input()
    left_list, right_list = parse_input(data)
    left_list, right_list = handle_complex_input(left_list, right_list)

    object_list = []
    object_list = get_list_of_objects(left_list, right_list)
    object_list.sort(key=sort_get_degree, reverse=True)

    handle_int_or_float(object_list)

    cleaned_object_list = []
    cleaned_object_list = clean_object_list(object_list)

    reduced_form(cleaned_object_list)
    degree = handle_degree(cleaned_object_list)

    abc = ()
    abc = solve_equation(degree, cleaned_object_list)
    if to_plot == 'Y':
        plot(abc)
