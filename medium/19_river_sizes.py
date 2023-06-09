def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(visited)):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop() # DFS
        i = currentNode[0]
        j = currentNode[1]
        
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
            
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)
        
def getUnvisitedNeighbors(i, j, matrix, visited):
    # up to 4 unvisited neighbors
    unvisitedNeighbors = []
    
    # there are nodes above and not visited
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    
    # there are nodes below and not visited
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
        
    # there are nodes on the left and not visited
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
        
    # there are nodes on the right and not visited
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
        
    return unvisitedNeighbors

print(str(riverSizes([[1,1,1],[1,1,0],[1,0,1]])))