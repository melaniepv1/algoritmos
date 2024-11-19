'''
Input:
- graph
- start
- end
Output:
- shortestPath
- distance
'''
def dijsktra(graph, start, end):

  numNodes = len(graph)
  distances = [float("inf")] * numNodes
  distances[start] = 0
  previousNodes = [-1] * numNodes
  visited = [False] * numNodes

  for _ in range(numNodes):

    currentNode = -1
    for i in range(numNodes):
      if not visited[i] and (currentNode == -1
                             or distances[i] < distances[currentNode]):
        currentNode = i

    if currentNode == -1 or distances[currentNode] == float("inf"):
      break

    visited[currentNode] = True

    for neighbor in range(numNodes):
      if graph[currentNode][neighbor] != float(
          "inf") and not visited[neighbor]:
        newDistance = distances[currentNode] + graph[currentNode][neighbor]
        if newDistance < distances[neighbor]:
          distances[neighbor] = newDistance
          previousNodes[neighbor] = currentNode

  path = []
  current = end

  if distances[end] == float("inf"):
    return [], float("inf")

  while current != -1:
    path.insert(0, current)
    current = previousNodes[current]

  return path, distances[end]
