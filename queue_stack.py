#Implement a Queue With Two Stacks
s1 = [1,2,3,4]
s2 = []

def enqueue(item):
    while(len(s2) > 0):
        s1.append(s2.pop())
    s1.append(item)

def dequeue():
    while(len(s1) > 0):
        s2.append(s1.pop())
    print(s2.pop())

dequeue()
dequeue()
dequeue()
dequeue()
enqueue(5)
dequeue()
