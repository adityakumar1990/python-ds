# Q - Find a number in the array such that all the elements
# in the array are divisible by it

# A - just find the min in the array and check if all the other elements
# are divisble by it

import sys

def check(arr):
    min = sys.maxsize
    for i in arr:
        if i < min:
            min = i
    for i in arr:
        if not i % min == 0:
            return False
    return True


arr = [20,10,15,5,100,200, 201]

print(check(arr))

#-----------------------------------------------------------------------#

def findDivisor(arr):
    if len(arr) == 0:
        return "Zero Length Array !!"
    elif len(arr) == 1:
        return f"arr[0]"
    else:
        arr.sort()
        for ele in arr[1:]:
            if ele % arr[0] != 0:
                return ("No such Element present in Array")
    return f"{arr[0]} is the element !!" 
