#!/usr/bin/env python3

# Created by: Matthew Meech
# Created on: Sep 2021
# This program calculates the area and perimeter of a circle
#    with radius 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 20mm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 20 ** 2))
    print("Perimeter is {} mm.".format(2 * math.pi * 20))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
