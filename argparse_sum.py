#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description="This programs displays the sum of two passed float values")
parser.add_argument("num1", type=int, help="Enter an float value")
parser.add_argument("num2", type=int, help="Enter an float value")

args = parser.parse_args()
square = float(args.num1) + float(args.num2)

print("The sum is:", square)

