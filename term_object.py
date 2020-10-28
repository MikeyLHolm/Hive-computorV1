import sys


class TermObject(object):
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree


def get_term_object(coeff, degree):

    term = TermObject(coeff, degree)
    return term


def get_coeff_and_degree(term):
    print('get coeff and degree from', term)
    #check until i, excluding i and check i+1 to end instead enumerate.
    if term.upper().find("X") != -1:
        for i, c in enumerate(term):
            if c.upper() == 'X':
                print(c)
                coeff = term[0:i - 1]
                degree = term[i + 1:]
                print(coeff)
                print(degree)
    else:
        sys.exit("No X in a term, EXIT")
    return coeff, degree


def opposite_sign(term):
    print(type(term))
    if term == '0':
        return
    if term[0] == "-":
        return term[1:]
    else:
        return ("-" + term)


def get_list_of_objects(left_data, right_data):
    #init values
    object_list = []
    coeff = 0
    degree = -1

    # add check for same degree
    for data in left_data:
        coeff, degree = get_coeff_and_degree(data)
        print(coeff, degree)
        term_object = get_term_object(coeff, degree)
        print(term_object.coeff)
        print(term_object.degree)
        object_list.append(get_term_object(coeff, degree))

    for data in right_data:
        coeff, degree = get_coeff_and_degree(data)
        print(coeff, degree)
        term_object = get_term_object(coeff, degree)
        print(term_object.coeff)
        print(term_object.degree)
        object_list.append(get_term_object(opposite_sign(coeff), degree))

    return object_list

