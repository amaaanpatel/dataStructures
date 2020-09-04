#quick sort
def quickSort(array):
    #base case if array lenth is 1
    if len(array) < 2: 
        return array
    else :
        pivot = array[0]
        # store all the elemsnts less than pivot in this list
        less_than_pivot = [i for i in array[1:] if i <= pivot]
        # store all the elemsnts geater than pivot in this list
        more_than_pivot = [i for i in array[1:] if i > pivot]

        #call quick sort recurservely
        return quickSort(less_than_pivot) + [pivot] + quickSort(more_than_pivot)

print(quickSort([10,5,2,3,20])) 