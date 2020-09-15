#find the maximunm length largest consicutaive intergers in a list
#https://www.youtube.com/watch?v=XXLVi2y2GrY&t=1312s
# [5,2,99,3,4,1,100] => max([99,100],[1..5])
#answer 5 cause 12345 has length 5 consicutaive

def find_maximum_length_sequence(array):
    visited = [False] * len(array)
    length = 0
    max_length = 0
    #create set form array to check if number in set
    array_set = set(array)
    for i in range(0,len(array)):
        if not visited[i]:
            visited[i] = True
            length += 1
        
        #check forward consicutive number
        forward = array[i] +1
        while forward in array_set:
            visited[array.index(forward)] = True
            length += 1
            forward += 1
        
        backward = array[i] - 1
        while backward in array_set:
            visited[array.index(backward)] = True
            length += 1
            backward -= 1
        max_length = max(max_length,length)
        length = 0
    print(max_length)
find_maximum_length_sequence([5,2,99,3,4,1,100])