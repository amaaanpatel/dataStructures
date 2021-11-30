#longest palindrom substring
import math
def palindrom(string):
    # print(string)
    letter = ''
    for i in range(0,len(string)-1):
        letter = string[i]
        for k in range(i+1,len(string)):
            letter += string[k]
            # print(letter)
            loop = math.floor(len(letter) / 2)

            for j in range(loop):
                if(letter[j] == letter[j -1]):
                    print(letter)




palindrom('abaxyzzyxf')