import sys


def plot_or_not():
    to_plot = input("Plot graph? (Y/N): ").upper()
    if to_plot != 'Y' and to_plot != 'N':
        raise SystemExit('Plot graph? -answer must be either Y or N')
    return to_plot

def read_input():
    to_plot = plot_or_not()
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        return arg, to_plot
    else:
        raise SystemExit('usage: python3 computor.py "[equation]"')

    # equation = input("Enter the equation: ")
    # return equation


def parse_input(data):
    data = data.replace(" ", "").replace("^", "").replace("-", "+-")
    data = data.split("=")
    return data[0].split("+"), data[1].split("+")


def remove_empty_items(left_data, right_data):
    cleaned_left_list = [x for x in left_data if x]
    cleared_right_list = [x for x in right_data if x]
    return cleaned_left_list, cleared_right_list
