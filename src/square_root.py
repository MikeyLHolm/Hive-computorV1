# Function to return the square root of
# a number using Newtons method
def square_root(n):

    if n < 0:
        raise SystemExit("n is smaller than 0. Can't solve sqrt.")

    tolerance_level = 0.00001
    x = n
    count = 0

    while (1):
        count += 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < tolerance_level):
            break
        x = root

    return root
