#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description="This programs displays the sum of two passed float values")
parser.add_argument("num", type=int,nargs=2, help="Enter two int value")

args = parser.parse_args()
square = float(args.num[0]) + float(args.num[1])

print("The sum is:", square)

