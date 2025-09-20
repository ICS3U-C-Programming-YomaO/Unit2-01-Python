#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: September 19, 2025
# This program calculates the area and perimeter of a rectangle with a user input


print(
    "Welcome to this program, the computer will calculate the area and perimeter with your input!"
)
# get length and width from the user
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# then calculate the perimeter and area
area = length * width
perimeter = 2 * (length + width)

# calculate and show the answer
print("Area: ", area)
print("perimeter: ", perimeter)
