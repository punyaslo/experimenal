#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description="This programs displays the square of a passed value")
parser.add_argument("num", type=int, help="Enter an integer value")

args = parser.parse_args()
square =  args.num ** 2

print("The square value is:", square)

