class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        graph = dict()
        for i in range(0,numCourses):
            graph[i] = [[],[]] #[[parents],[children]]
        
        for edge in prerequisites:
            graph[edge[0]][0].append(edge[1]) #add parent
            graph[edge[1]][1].append(edge[0]) #add child
            
        freeNode = []
        result = []
        for i in range(0,numCourses):
            if not graph[i][0]: 
                freeNode.append((i,graph[i][1]))
                result.append(i)
        while freeNode:
            node = freeNode.pop(0)
            for child in node[1]:
                graph[child][0].remove(node[0])
                if not graph[child][0]: 
                    freeNode.append((child,graph[child][1]))
                    result.append(child)
        if len(result) == numCourses: return result
        else: return []