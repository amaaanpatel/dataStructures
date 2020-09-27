#graph 
graph = {}
#start node
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# fin(finish)
#node a
graph['a'] = {}
graph['a']['fin'] = 1
#node b
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
#node finisg
graph['fin'] = {}

# cost tracking graph
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b']=2
costs['fin'] = infinity

#parent tracking graph
parent = {}
parent['a'] = "start"
parent['b']= "start"
parent['fin'] = None

# keep track of processed node
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = cost
            lowest_cost_node = node 
    return lowest_cost_node

#diktras alog
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        newcost = cost + neighbors[n]
        if costs[n] > newcost:
            costs[n] = newcost
            parent[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(pare)