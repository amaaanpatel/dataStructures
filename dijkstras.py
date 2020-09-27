#graph
graph = {}
graph["start"]={}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 5
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"] = {}
graph["d"]["fin"] = 1
graph["fin"] = {}


#cost hashtable set the initial cost for start node
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["fin"] = float("inf")

#parent table to maintain the route taken
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed_Nodes = []


def get_lowest_node_with_lowest_cost(node):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for cost in costs:
        if costs[cost] < lowest_cost and cost not in processed_Nodes:
            lowest_cost = costs[cost] 
            lowest_cost_node = cost
    # print(lowest_cost_node)
    print(lowest_cost_node, 'his is lowest node')
    return lowest_cost_node

node = get_lowest_node_with_lowest_cost(costs)
while node is not None:
        #get the cost of current node
        cost = costs[node]
        #get the childs of current node node loop over its
        neibours = graph[node]
        #loop overs the child current node
        for n in neibours.keys():
            # print(n)
            #calculate the new cost 
            print(cost , neibours[n])
            new_cost = cost + neibours[n]
            # print(costs[n] , new_cost)
            #chcek and upadte the cost table in with the childs of current node
            if costs.get(n) is not None and costs[n] > new_cost:
                costs[n] = new_cost
                #update the parent hastable to update the path
                parents[n] = node 
            elif  costs.get(n) is None :
                costs.update({n:cost + neibours[n]})
                parents.update({n:node})    
        #mak this node as visited
        processed_Nodes.append(node)
        node = get_lowest_node_with_lowest_cost(costs)
print(costs)
print(parents)
        
    
