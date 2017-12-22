# Created by: Gavin Zhou
# Created on: Dec 2017 
# Created for: ICS3U

from numpy import random

def find_largest_value(array):
    largest_value = float(0)
    for index in array:
        if largest_value < index:
            largest_value = index
    return largest_value

my_array = []
for largest_random in range(0, random.randint(1, 25)):
    my_array.append(random.randint(1, 50))
print(my_array)
print(find_largest_value(my_array))






