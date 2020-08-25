def selectionSort(array):
    new_Array = []
    for i in range(len(array)):
        index = 0
        small = 0
        for j in range(len(array)):
            if array[j] > small:
                small = array[j]
                index = j
        new_Array.append(array.pop(index))
    return new_Array

print(selectionSort([5,3,8,4]))