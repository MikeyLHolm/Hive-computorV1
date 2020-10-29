from square_root import square_root


def is_prime(n):
    # pre-condition: n is a nonnegative integer
    # post-condition: return True if n is prime and False otherwise.
    if n < 2:
         return False
    if n % 2 == 0:
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True


def get_prime_factors(number):
    # create an empty list and later I will
    # run a for loop with range() function using the append() method to add elements to the list.
    prime_factors = []

    # First get the number of two's that divide number
    # i.e the number of 2's that are in the factors
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    # After the above while loop, when number has been
    # divided by all the 2's - so the number must be odd at this point
    # Otherwise it would be perfectly divisible by 2 another time
    # so now that its odd I can skip 2 ( i = i + 2) for each increment
    for i in range(3, int(square_root(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i


    # Here is the crucial part.
    # First quick refreshment on the two key mathematical conjectures of Prime factorization of any non-Prime number
    # Which is - 1. If n is not a prime number AT-LEAST one Prime factor would be less than sqrt(n)
    # And - 2. If n is not a prime number - There can be AT-MOST 1 prime factor of n greater than sqrt(n).
    # Like 7 is a prime-factor for 14 which is greater than sqrt(14)
    # But if the above loop DOES NOT go beyond square root of the initial n.
    # Then how does that greater than sqrt(n) prime-factor
    # will be captured in my prime factorization function.
    # ANS to that is - in my first for-loop I am dividing n with the prime number if that prime is a factor of n.
    # Meaning, after this first for-loop gets executed completely, the adjusted initial n should become
    # either 1 or greater than 1
    # And if n has NOT become 1 after the previous for-loop, that means that
    # The remaining n is that prime factor which is greater that the square root of initial n.
    # And that's why in the next part of my algorithm, I need to check whether n becomes 1 or not,
    if number > 2:
        prime_factors.append(int(number))

    return prime_factors


def prime_factorization(a, b, discriminant):
    prime_factors = []
    #discriminant = -240
    if discriminant < 0:
        discriminant *= -1

    print(- b / (2 * a), " + i", square_root(discriminant))
    print(- b / (2 * a), " - i", square_root(discriminant))
    if is_prime(discriminant):
        prime_factors.append(discriminant)
    else:
        prime_factors = get_prime_factors(discriminant)
    for factor in prime_factors:
        print(factor)

    return prime_factors
