import sys


class TermObject(object):
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree


def get_term_object(coeff, degree):

    term = TermObject(coeff, degree)
    return term


def get_coeff_and_degree(term):
    if term.upper().find("X") != -1:
        for i, c in enumerate(term):
            if c.upper() == 'X':
                coeff = term[0:i - 1]
                degree = term[i + 1:]
    else:
        sys.exit("No X in a term, EXIT")
    return coeff, degree


def opposite_sign(term):
    if term == '0':
        return
    if term[0] == "-":
        return term[1:]
    else:
        return ("-" + term)


def handle_dupl_degree(object_list, term_object):
    #iterate list to find dup degree
    #if found, update coeff
    for obj in object_list:
        if obj.degree == term_object.degree:
            obj.coeff = float(obj.coeff) + float(term_object.coeff)
            return 1
    return 0

def get_list_of_objects(left_data, right_data):
    #init values
    object_list = []
    coeff = ""
    degree = ""

    for data in left_data:
        coeff, degree = get_coeff_and_degree(data)
        term_object = get_term_object(coeff, degree)
        if not handle_dupl_degree(object_list, term_object):
            object_list.append(get_term_object(coeff, degree))

    for data in right_data:
        coeff, degree = get_coeff_and_degree(data)
        term_object = get_term_object(opposite_sign(coeff), degree)
        if not handle_dupl_degree(object_list, term_object):
            object_list.append(term_object)

    return object_list
