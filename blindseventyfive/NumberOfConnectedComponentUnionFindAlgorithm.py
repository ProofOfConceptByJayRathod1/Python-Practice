from typing import (
    List,
)


# union find algorithm, similar problem : leetcode 547
class NumberOfConnectedComponentUnionFindAlgorithm:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # in union find algorithm, one component of a graph will have only one parent. irrespective of the edges, because here our matter of concern is not edges but the number of components.
        # parent array indices represents nodes and values will represent it's parents after calculation in union method
        parentArray = [iter for iter in range(n)]
        # rank array indices will be appended as we connect child nodes to the parent node.
        ranks = [1] * n

        # below function will find the absolute parent of a certain node.
        def findRootParentOfANode(node1):
            result = node1
            # at some point, as we are representing 'indices' in parentArray as vertices the parent index and value will be the same. that is the purpose of the while loop , to find the parent.
            while (result != parentArray[result]):
                # path compression
                parentArray[result] = parentArray[parentArray[result]]
                result = parentArray[result]
            # in the below result variable the parent of the respective node will be returned
            return result

        # the below method findUnion will actually update the ranks
        def findUnion(node1, node2):
            parent1, parent2 = findRootParentOfANode(node1), findRootParentOfANode(node2)
            # it means we didn't perform a union so we will return 0, as only when we will perform a union we will increase tehe value
            if parent1 == parent2:
                return 0
            # below are the scenarios when the components are differnt
            # if rank of parent2 is greater than parent1 then make the parent of parent1 as parent2
            # else the opposite
            if ranks[parent2] > ranks[parent1]:
                parentArray[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            #     else if rank of parent1 is greater than parent2
            else:
                parentArray[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            # if the parents are different, we make the parents common for the same component.
            return 1

        # result will decrease as we keep on finding two nodes with same parents, else it wont decrease, hence in the end returning us with the number of components./
        res = n
        #
        for node1, node2 in edges:
            res -= findUnion(node1, node2)
        return res
