# Programmer: Noah
# Description: Find Formula for a cylinder 
from math import pi


#Find number values
diameter = input ("Enter the diameter ")
height = input ("Enter the height ")
diameter = float(diameter)
height = float (height)

#Calculate for surface area
radius = diameter / 2
lateral_surface = 2 * pi * radius * height
base = pi * radius ** 2
total = 2 * base + lateral_surface

#Calculate for volume
volume = base * height
volume_two = pi * radius ** 2 * height
volume = volume + volume_two

#print
print ()
print (f"The volume is {volume}")
print (f"The surface area is {total}")


