def save_terms_left(left):
    print("L terms are: ", left)

    for term in left:
        if term.find("X") != -1:
            print(term)
            for i, c in enumerate(term):
                if c == "X":
                    print(c)
                    print(term[i + 1])
                    if term[i + 1] == "0":
                        constants.append(term[0:i - 1])
                    elif term[i + 1] == "1":
                        x_1.append(term[0:i - 1])
                    elif term[i + 1] == "2":
                        x_2.append(term[0:i - 1])
                    else:
                        sys.exit("Other degrees not supported, EXIT")
        else:
            sys.exit("No X in a term, EXIT")


def save_terms_right(right):
    print("R terms are: ", right)

    for term in right:
        if term.find("X") != -1:
            for i, c in enumerate(term):
                if c == "X":
                    if term[i + 1] == "0":
                        constants.append(opposite_sign(term[0:i - 1]))
                    elif term[i + 1] == "1":
                        x_1.append(opposite_sign(term[0:i - 1]))
                    elif term[i + 1] == "2":
                        x_2.append(opposite_sign(term[0:i - 1]))
                    else:
                        sys.exit("Other degrees not supported, EXIT")
        else:
            sys.exit("No X in a term, EXIT")


def return_degree(side):
    degree = -1
    temp_degree = ""
    side_len = len(side)
    if side.find("X") != -1:
        for i, c in enumerate(side):
            if c == "X":
                j = i
                while (j + 1) < side_len and side[j + 1].isdigit():
                    temp_degree = temp_degree + side[j + 1]
                    j += 1
                if int(temp_degree) > degree:
                    degree = int(temp_degree)
                temp_degree = ""
    else:
        return 0
    return(degree)


def get_degree(data):
    degree_l = return_degree(data[0])
    degree_r = return_degree(data[1])
    if degree_l >= degree_r:
        return degree_l
    else:
        return degree_r


def calc_constants():
    constant = 0
    for x in constants:
        constant += int(x)
    return constant


def calc_first_degree():
    first_degree = 0
    for x in x_1:
        first_degree += int(x)
    return first_degree


def calc_second_degree():
    second_degree = 0
    for x in x_2:
        second_degree += float(x)
    return second_degree
