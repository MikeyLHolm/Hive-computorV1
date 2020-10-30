import sys


def plot_or_not():
    to_plot = input("Plot graph? (Y/N): ").upper()
    if to_plot != 'Y' and to_plot != 'N':
        raise SystemExit('Plot graph? -answer must be either Y or N')
    return to_plot


def read_input():
    #to_plot = plot_or_not()
    to_plot = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        return arg, to_plot
    else:
        raise SystemExit('usage: python3 computor.py "[equation]"')

    # equation = input("Enter the equation: ")
    # return equation


def remove_empty_items(left_data, right_data):
    cleaned_left_list = [x for x in left_data if x]
    cleared_right_list = [x for x in right_data if x]
    return cleaned_left_list, cleared_right_list


def parse_input(data):
    data = data.replace(" ", "").replace("^", "").replace("-", "+-")
    data = data.split("=")
    print(data[0])
    print(data[1])
    left_data = data[0].split("+")
    right_data = data[1].split("+")
    left_data, right_data = remove_empty_items(left_data, right_data)
    return left_data, right_data


def handle_zero_degree_form(left_list, right_list):
    left_form_handled = [obj + '*X0' if not 'X' in obj.upper() else obj for obj in left_list]
    right_form_handled = [obj + '*X0' if not 'X' in obj.upper() else obj for obj in right_list]
    return left_form_handled, right_form_handled


def handle_no_coeff():
    pass


def handle_no_degree():
    pass
