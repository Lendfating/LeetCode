#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None: return None
        start_node = UndirectedGraphNode(node.label)
        # add old node into to-copy list, so we needn't find it for each loop 
        maps, to_clone = {node.label:start_node}, [node]
        while len(to_clone)>0:
            n = to_clone.pop(0)
            for nb in n.neighbors:
                if not maps.has_key(nb.label):
                    maps[nb.label] = UndirectedGraphNode(nb.label)
                    to_clone.append(nb)
                maps[n.label].neighbors.append(maps[nb.label])
        return start_node
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph1(self, node):
        # A recursive version
        return self.__cloneGraph(node, {})
        
    def __cloneGraph(self, node, map):
        if node is None: return None
        clone_node = UndirectedGraphNode(node.label)
        map[node.label] = clone_node
        for nb in node.neighbors:
            if map.has_key(nb.label):
                clone_node.neighbors.append(map[nb.label])
            else:
                clone_node.neighbors.append(self.__cloneGraph(nb, map))
        return clone_node
        

if __name__ == '__main__':
    pass
