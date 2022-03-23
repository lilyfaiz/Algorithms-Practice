'''
    Min Heap Construction:
    Build a min heap given an input array and implement the
    following functionality:

    buildHeap
    insert
    remove
    peek
    siftUp
    siftDown
    swap

    Last Practiced: 2022-03-16 07:50:50
'''
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParent = (len(array) - 2) // 2
        for i in reversed(range(firstParent + 1)):
            self.siftDown(array, i, len(array) - 1)
        return array

    def siftDown(self, heap, currentIndex, endIndex):
        childOneIndex = currentIndex * 2 + 1
        while childOneIndex <= endIndex:
            childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex
            if heap[indexToSwap] < heap[currentIndex]:
                self.swap(heap, indexToSwap, currentIndex)
                currentIndex = indexToSwap
                childOneIndex = currentIndex * 2 + 1
            else:
                return # heap is already in built

    def siftUp(self, heap, currentIndex):
        parentIndex = (currentIndex - 1) // 2
        while parentIndex >= 0 and heap[parentIndex] > heap[currentIndex]:
            self.swap(heap, currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def peek(self):
        if len(self.heap) >= 1: return self.heap[0]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        valueToPop = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return valueToPop

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)
        
    def swap(self, heap, left, right):
        heap[left], heap[right] = heap[right], heap[left]

def dijkstrasAlgorithm(start, edges):
    numberOfEdges = len(edges)
    minDistanceFromStart = [float('inf')] * numberOfEdges
    minDistanceFromStart[start] = 0
    visited = set()
    
    while len(visited) < numberOfEdges:
        currentVertex, distanceFromStartToCurrentVertex = getNextClosestUnvisitedNode(minDistanceFromStart, visited)
        visited.add(currentVertex)
        
        if distanceFromStartToCurrentVertex == float('inf'): break # Closest node is unreachable. Finish algorithm
        
        for edge in edges[currentVertex]:
            currentVertextNeighbor, distanceFromCurrentVertexToNeighbor = edge
            if currentVertextNeighbor in visited: continue
            
            newDistanceFromStartToNeighbor = distanceFromStartToCurrentVertex + distanceFromCurrentVertexToNeighbor
            currentDistanceFromStartToNeighbor = minDistanceFromStart[currentVertextNeighbor]
            
            if newDistanceFromStartToNeighbor < currentDistanceFromStartToNeighbor:
                minDistanceFromStart[currentVertextNeighbor] = newDistanceFromStartToNeighbor
                
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStart))

def getNextClosestUnvisitedNode(minDistanceFromStart, visited):
    candidateVertex = None
    candidateDistance = float('inf')
    
    for vertex, distance in enumerate(minDistanceFromStart):
        if vertex in visited: continue
        if distance <= candidateDistance:
            candidateVertex = vertex
            candidateDistanxe = distance
            
    return candidateVertex, candidateDistance


distances = [
    [[1,7]],
    [[2,6],[3,20],[4,3]],
    [[3,14]],
    [[4,2]],
    [],
    []
    ]
start = 0

print(dijkstrasAlgorithm(start, distances))