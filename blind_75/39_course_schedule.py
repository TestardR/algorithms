# O(n + p) nodes + prerequisites
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting: # visiting a course twice, there is a loop
                return False
            
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            preMap[crs] = [] # reset as prerequisites are visited
            
            return True

        for c in range(numCourses): # we loop as our graph my not be connected
            if not dfs(c):
                return False
        return True