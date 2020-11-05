# Hive-computorV1
A Hive school procject to write a program that solves a polynomial equation of degree less than or equal to 2. 2nd degree polynomial can be called also quadratic equation.

## How to use:

Clone repo and enter dir:
```
https://github.com/MikeyLHolm/Hive-computorV1.git
cd Hive-computorV1
```
Run the program:
```
./computor
or
python3 computor.py
```
Enter equation string without quotes and choose to plot the graph:
```
Enter equation: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
Plot graph? (Y/N): y
```

Run tests:
```
python3 test.py
```

## Solution:
Cleaned up list of terms as strings is sent to object_handler. Each term is saved to an object with two values: coefficient and degree. Then objects are appended to a list if no duplicates of the degree is found. Otherwise the coeff of that degree is updated.

Then list in reduced form is sent to solver and values of a, b & c to plotter.

## Bonuses:
* A single coefficient ("4") is considered to be a factor of X ^ 0.
* An absent power ("4 * X") is considered to be 1.
* An absent coefficient ("X ^ 6") is considered to be equal to 1.
* The powers can be in an arbitrary order, possibly repeated.
* Unittests
* Plotting

## Limitations:
* Input must be of certain form. There must be '*' between coefficent and X.
* On some rare cases float conversion limitations creates inaccuracies: calculations ending with small figures migth be converted to ints instead floats.
* Some bigger degrees don't always get sorted in right order. Reduced form can end up like:<br>
  3 * X^2 + 4 * X^33 - 1 * X^1 + 7 * X^0 = 0

## Possible improvements:
* Add solver for higher degrees (cubic-->).
* Replace lists with something more effective.
* More use out of the object.
* Remove limitations of '*'.

## Grade:
**122/100**

_completed: 05.11.2020_
