# Programmer: Noah
# Description: Mystery mart
from math import ceil
from random import uniform

#Generate random decimal and calculate
total =  uniform (0.0,1000.0)
bills = total / 100
bills = float (bills)
bills = ceil (bills)
change = bills * 100 - total


# Print scentence
print ("Welcome to Mystery Mart")
print (f"This product costs ${total:,.2f}")
print (f"Please pay {bills} hundred-dollar bills")
print (f"Your change is ${change:,.2f}")



