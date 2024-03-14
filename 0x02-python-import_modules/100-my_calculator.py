#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    args_num = len(argv)
    if args_num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    opertor = argv[2]
    b = int(argv[3])
    if opertor == '+':
        print(f"{a} {opertor} {b} = {add(a, b)}")
    elif opertor == '-':
        print(f"{a} {opertor} {b} = {sub(a, b)}")
    elif opertor == '*':
        print(f"{a} {opertor} {b} = {mul(a, b)}")
    elif opertor == '/':
        print(f"{a} {opertor} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
