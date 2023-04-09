import collections
from collections import deque


class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # as number of edges for connected graph with n vertices will be equal to n-1
        if len(edges) != n - 1:
            return False

        adjacencyList = collections.defaultdict(list)
        for node1, node2 in edges:
            adjacencyList[node1].append(node2)
            adjacencyList[node2].append(node1)

        visitedVertices = set()
        queueVertices = deque()

        queueVertices.append(0)
        visitedVertices.add(0)


        while queueVertices:
            # pop the leftmost element in the dequeue, for deque to behave as a queue
            currentNode = queueVertices.popleft()

            for adjacentNodeOfCurrentNode in adjacencyList[currentNode]:
                if adjacentNodeOfCurrentNode not in visitedVertices:
                    queueVertices.append(adjacentNodeOfCurrentNode)
                    visitedVertices.add(adjacentNodeOfCurrentNode)

        return len(visitedVertices) == n 
