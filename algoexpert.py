# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array,multiplier = 1):
  if isinstance(array,int):
    return array
  else:
    sum = 0
    for i in array:
      if isinstance(i,int):
          sum += i
      else: 
          sum += productSum(i , multiplier + 1)
    return multiplier * sum



print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))