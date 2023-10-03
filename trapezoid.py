# Programmer: trapezoid
# Description: measure a trapezoid

#convert 2 numbers
bottom = input ("Enter the long base length ")
top = input ("Enter the short base length ")
height = input ("Enter the altitude ")
bottom = int(bottom)
top = int(top)
height = int(height)


area = (bottom + top) / 2 * height

print (f"The area is {area}")