"""
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""
import numpy
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
print("x**y =", x**y)
print("log(x) =", numpy.log2(x))
