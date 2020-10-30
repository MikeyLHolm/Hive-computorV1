# Change mantissa to better name as this truly isn't mantissa afaik!
def str_to_float_or_int(value_str, ShowExtended=False):
    isfloat = True
    value = float(value_str)
    numberParsed = value_str.split(".")
    if len(numberParsed) > 1:
        integer = numberParsed[0]
        mantissa = numberParsed[1]
        if integer.strip('-').isdecimal() and mantissa.isdecimal():
            if int(mantissa) == 0:
                isfloat = False
                value = int(integer)
        elif integer.strip('-').isdecimal():
            isfloat = False
            value = int(integer)
    else:
        isfloat = False
        value = int(value_str)
    if ShowExtended:
        print("testValue: " + value_str + " | splits into: ",
                numberParsed,"\n value: ", value)
        if isfloat:
            print("It's a <float> (;o)\n")
        else:
            print("It's an <int> {:o)~\n")

    return value


def handle_int_or_float(object_list):
    for term in object_list:
        term.coeff = str_to_float_or_int(str(term.coeff))
