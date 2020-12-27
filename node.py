from math import inf

class Node: 
    def __init__(self, id):
        self.__id = id
        self.__neighbors = {}
        self.__shortest_dist = inf
        self.__prev_node = None

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNeighbors(self):
        return self.__neighbors

    def setNeighbor(self, node, dist):
        self.__neighbors[node] = dist

    def getShortestDist(self):
        return self.__shortest_dist

    def setShortestDist(self, dist):
        self.__shortest_dist = dist

    def getPrevNode(self):
        return self.__prev_node

    def setPrevNode(self, node):
        self.__prev_node = node

    def __str__(self):
        return "\nNode: "+self.__id+"\nAdjacents:\n"+"\n".join(str(node.__id) + ", " + str(weight) for node, weight in self.__neighbors.items()) + "\nShortest distance: "+ str(self.__shortest_dist) + "\nPrevious node: "+ str(self.__prev_node.__id if self.__prev_node != None else "-")