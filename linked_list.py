import sys


class Node:
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None


    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.coeff, 'x^', printval.degree)
            printval = printval.nextval


    def AtBegining(self, coeff, degree):
        NewNode = Node(coeff, degree)

        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode


    def Inbetween(self,middle_node, coeff, degree):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(coeff, degree)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


    def AtEnd(self, coeff, degree):
        NewNode = Node(coeff, degree)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode


def find_same_degree():
    print('return node here')



def get_coeff_and_degree(term):
    print('get coeff and degree from', term)
    #check until i, excluding i and check i+1 to end instead enumerate.
    if term.find("X") != -1:
        for i, c in enumerate(term):
            if c == "X":
                print(c)
                coeff = term[0:i - 1]
                degree = term[i + 1:]
                print(coeff)
                print(degree)
                # if term[i + 1] == "0":
                #     constants.append(term[0:i - 1])
                # elif term[i + 1] == "1":
                #     x_1.append(term[0:i - 1])
                # elif term[i + 1] == "2":
                #     x_2.append(term[0:i - 1])
                # else:
                #     sys.exit("Other degrees not supported, EXIT")
    else:
        sys.exit("No X in a term, EXIT")
    return coeff, degree


def parse_to_linked_list(left, right):
    coeff = 0
    degree = -1

    coeff, degree = get_coeff_and_degree(left[0])
    #get_coeff_and_degree(left[0])
    list_equation = SLinkedList()
    list_equation.headval = Node(coeff, degree)
    e2 = Node(4, 1)
    e3 = Node(-9.3, 2)

    list_equation.headval.nextval = e2
    e2.nextval = e3

    # list_equation.AtBegining("Sun")
    # list_equation.AtEnd("Thu")

    list_equation.listprint()
    return list
