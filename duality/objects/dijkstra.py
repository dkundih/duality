graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
 

def dijkstra(nodes, origin, destination):
    shortest_distance = {}
    predecessor = {}
    nodecollection = nodes
    path = []
    for node in nodecollection:
        shortest_distance[node] = float('inf')
    shortest_distance[origin] = 0
 
    while nodecollection:
        minNode = None
        for node in nodecollection:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        nodecollection.pop(minNode)
 
    currentNode = destination
    while currentNode != origin:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, origin)
    if shortest_distance[destination] != float('inf'):
        print('Shortest distance is ' + str(shortest_distance[destination]))
        print('And the path is ' + str(path))
 
dijkstra(graph, 'a', 'd')