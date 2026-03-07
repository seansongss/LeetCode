class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereq_dict = {i: [] for i in range(numCourses)}
        req_set = set()

        for i, j in prerequisites:
            prereq_dict[j].append(i)
            req_set.add(i)

        def dfs(prereq_dict, visited, start):
            for course in prereq_dict[start]:
                if course in visited:
                    return False
                if not dfs(prereq_dict, visited + [course], course):
                    return False
            
            prereq_dict[start] = []

            return True
    
        for i in req_set:
            if not dfs(prereq_dict, [i], i):
                return False
        return True
