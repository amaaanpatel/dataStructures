#implementing graps (directed graph —the relationship is only one way) using hash table 
#create a dict (hash tabel)
graph = {}
#your neibour you -> alice,bob,claire
#bob neibour -> anui,peggy
# and so on ......
#This is called a directed graph—the relationship is only one way. So Anuj is Bob’s neighbor, but Bob isn’t Anuj’s neighbor.
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice']=['peggy']
graph['claire'] =['thom','jonny']

print(graph)