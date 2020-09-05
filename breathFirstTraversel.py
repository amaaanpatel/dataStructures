#breath first traversal
from collections import deque

def search(name,graph):
    #create a deque
    search_queue = deque()
    print(search_queue)
    #searched elements 
    searched = []
    #start the search with the given name 
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()
        print(person)
        if not person in searched:
            if checkMangoSeller(person):
                print(person + ' is mango seller')
                return True
            else : 
                print(graph[person])
                search_queue += graph[person]
                searched.append(person)
    return False

def checkMangoSeller(person):
    return person[-1] == 'm'

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice']=['peggy']
graph['claire'] =['thom','jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
print(graph)


search('you',graph)
#thom is the mango seller because it ends with m

