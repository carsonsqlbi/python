#! /usr/bin/env python3

x = input("Please enter a number: ")
x = int(x)

if x > 200:
    print("Greater than 200")
elif x > 100:
    print("Greater than 100, but less or equals to 200")
else:
    print("Less or equals to 100")
