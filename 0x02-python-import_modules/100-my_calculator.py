#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, operator[sys.argv[2]](a, b)))
