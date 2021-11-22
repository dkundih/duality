graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
 

def dijkstra(nodes, origin, destination):
    shortest_distance = {}
    predecessor = {}
    nodeCollection = nodes
    path = []
    for node in nodeCollection:
        shortest_distance[node] = float('inf')
    shortest_distance[origin] = 0
 
    while nodeCollection:
        closestNode = None
        for node in nodeCollection:
            if closestNode is None:
                closestNode = node
            elif shortest_distance[node] < shortest_distance[closestNode]:
                closestNode = node
 
        for secondaryNode, weight in graph[closestNode].items():
            if weight + shortest_distance[closestNode] < shortest_distance[secondaryNode]:
                shortest_distance[secondaryNode] = weight + shortest_distance[closestNode]
                predecessor[secondaryNode] = closestNode
        nodeCollection.pop(closestNode)
 
    liveNode = destination
    while liveNode != origin:
        try:
            path.insert(0, liveNode)
            liveNode = predecessor[liveNode]
        except KeyError:
            print('Path unavailable.')
            break
    path.insert(0, origin)
    if shortest_distance[destination] != float('inf'):
        print('Shortest distance is ' + str(shortest_distance[destination]))
        print('And the path is ' + str(path))
 
dijkstra(graph, 'a', 'e')