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
        raise SystemExit('No X in a term, EXIT')
    zero = '-0'
    if coeff == zero:
        print('rr')
        coeff == '0'
    return coeff, degree


def opposite_sign(term):
    if term == '0':
        return (term)
    if term[0] == '-':
        return term[1:]
    else:
        return ('-' + term)


def handle_dupl_degree(object_list, term_object):
    # protect when coeff = 0
    for obj in object_list:
        if term_object.coeff == '0':
            return 1
        if obj.degree == term_object.degree:
            obj.coeff = float(obj.coeff) + float(term_object.coeff)
            return 1
    return 0


def get_list_of_objects(left_data, right_data):
    object_list = []
    coeff = ""
    degree = ""

    for data in left_data:
        coeff, degree = get_coeff_and_degree(data)
        print(coeff, degree)
        print(type(coeff))
        if coeff == '0':
            print('coeff 0')
            continue
        term_object = get_term_object(coeff, degree)
        if not handle_dupl_degree(object_list, term_object):
            object_list.append(get_term_object(coeff, degree))

    for data in right_data:
        if data == '0':
            continue
        coeff, degree = get_coeff_and_degree(data)
        term_object = get_term_object(opposite_sign(coeff), degree)
        if not handle_dupl_degree(object_list, term_object):
            object_list.append(term_object)

    #remove terms with coeff of 0
    cleaned_object_list = [x for x in object_list if x.coeff != 0]

    return cleaned_object_list
