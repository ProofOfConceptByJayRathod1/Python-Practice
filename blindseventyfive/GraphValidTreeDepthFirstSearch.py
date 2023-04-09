from typing import (
    List,
)


class GraphValidTreeDepthFirstSearch:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # If there is no graph to traverse we will return true
        if not n:
            return True
        adjacencyList = {vertex: [] for vertex in range(n)}
        # create an adjacency list of an undirected graph
        for node1, node2 in edges:
            adjacencyList[node1].append(node2)
            adjacencyList[node2].append(node1)
        visitedVertices = set()

        # defining the below function inside another function so that the adjacencyList can be accessed without passing it as a parameter
        def depthFirstSearch(nodeForDepthFirstSearchTraversal, previousNode):
            if nodeForDepthFirstSearchTraversal in visitedVertices:
                return False
            visitedVertices.add(nodeForDepthFirstSearchTraversal)
            for neighborsOfCurrentNode in adjacencyList[nodeForDepthFirstSearchTraversal]:
                if neighborsOfCurrentNode == previousNode:
                    continue
                if not depthFirstSearch(neighborsOfCurrentNode, nodeForDepthFirstSearchTraversal):
                    return False
            return True

        '''returns true if there is no cycle AND the number of nodes exactly matches the visited set of vertices'''
        return depthFirstSearch(0, -1) and n == len(visitedVertices)
