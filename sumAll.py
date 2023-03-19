import math
def sumAll(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print("sum :", sumAll(1,2,3,45,6))

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

def rectangle_area():
    length = float(input("Get the length : "))
    width = float(input("Enter the width : "))
    area = length * width
    print("the area of thr rectaangle is", area)

def circle_area():
    radius = float(input("Enter the radius"))

    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is {:.2f}".format(area))
def main():
    shape_type = input("Get area for what shape : ")

    get_area(shape_type)