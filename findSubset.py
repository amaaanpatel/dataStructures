#Find all subsets of characters in a string. Example string "abc" should give
#[{a},{b},{c},{ab},{bc},{ac},{abcd}]

sub =  "abcd"
result = []

# for i in range(len(sub)):
#     for j in range(i,len(sub)):
#         result.append(sub[i:(j+1)])
# print(result)

def printSubString(input,output):
    print(input,output)
    if(len(input)==0):
        print("***************")
        print(output)
        return
    
    printSubString(input[1:],output+input[0])
    print("&&&&&&&&&&")
    print(input,output)
    printSubString(input[1:],output)

output = ""
input="abcd"
printSubString(input,output)