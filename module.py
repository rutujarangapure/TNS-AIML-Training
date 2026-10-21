import math

def perimeter(length, width=None):
    if width is None:
        return 4 * length  # Perimeter of a square
    else:
        return 2 * (length + width)  # Perimeter of a rectangle

def circle_area(radius):
    return math.pi * radius ** 2

    print("Module.py has been successfully loaded.")