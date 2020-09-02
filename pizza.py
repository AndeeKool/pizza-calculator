# print("What is the area of the pizza?")
diameter = int(input("What is the diameter of the pizza? "))
cost = int(input("How much does it cost producing the pizza? "))

from math import pi

radius = diameter / 2
area = round((pi * radius**2), 2)

efficiency = round((area / cost), 2)
print("The pizza efficiency is: " + str(area) + " cm^2" + " / " + "$" + str(cost) + " = " + str(efficiency))
