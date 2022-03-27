#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = lambda x: x**2
cube = lambda x: x**3

for num in NUMBERS:
    print(f"Number: {num}, square: {square(num)}, cube: {cube(num)}")
