import math
def binarySerch(blist,item):
    low = 0
    high = len(blist) - 1
    print(low,high)
    while low <= high:
        mid = math.floor((low + high) / 2)
        guess = blist[mid]
        if guess == item:
            return mid
        if item > guess:
            low = mid + 1
        else :
            high = mid - 1
    return None



print(binarySerch([1,2,3,4,5,6,7,8],5))

    
