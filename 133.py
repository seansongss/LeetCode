"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        cur_lst = [node]
        node_dict = {}
        while len(cur_lst) > 0:
            cur = cur_lst.pop(0)

            if cur.val not in node_dict.keys():
                node_dict[cur.val] = set()
            for neighbor in cur.neighbors:
                if neighbor.val not in node_dict.keys():
                    cur_lst.append(neighbor)
                node_dict[cur.val].add(neighbor.val)
        
        res_node = []
        for i in range(len(node_dict)):
            res_node.append(Node(val = i + 1))
        
        for i in range(len(res_node)):
            for val in node_dict[i+1]:
                res_node[i].neighbors.append(res_node[val-1])
        return res_node[0]