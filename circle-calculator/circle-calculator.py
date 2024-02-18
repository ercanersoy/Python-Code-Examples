# Circle Calculator - A circle calculator program
# Copyright (c) 2020-2024 Ercan Ersoy
# This file licensed under MIT License.

pi = 3.14

radius = int(input("Radius of circle: "))

circumference = radius * 2 * pi
area = pow(radius, 2) * pi

print("Circumference: ", end="")
print(circumference)

print("Area: ", end="")
print(area)