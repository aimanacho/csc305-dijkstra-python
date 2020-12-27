from node import Node

class Graph:

    def __init__(self):
        self.__node = []

    #node1 = origin, node2 = destination
    def add_unidirectional_edges(self, node1, node2, distance)
        # 1. declare two variable nodes
        n1 = n2 = None
        
        # 2. check if exist
        for x in self.__node:
            if x.getId()==node1:
                n1 = x
            if x.getId()==node2:
                n2 = x

        # 3. if n1 or n2 is None, create node1 / node2
        if n1 is None:
            n1 = Node(node1)
        if n2 is None:
            n2 = Node(node2)

        # add neighbour
        if n1 in n2.getNeighbors() and n2 in n1.getNeighbors():
            print("Is already neighbours")
        else
            n1.setNeighbor(n2,distance) # n1 ----> n2


    
    def add_bidirectional_edges( self, node1, node2, distance):
        #declaration of n1 and n2
        n1 = n2 = None

        #check if node1,node 2 exist , then assign the object to n1/n2
        for x in self.__node:
            if x.getId()== node1:
                n1 = x
            if x.getId()== node2:
                n2 = x
        
        #If node1 and node2 not exist, then create a new node to assign to n1/n2
        if n1 is None:
           n1 = Node(node1) 
        if n2 is None:
            n2 = Node(node2)

        #Set neighbour between edges
        #Check if 2 edges oredi a neihbor exist
        if n1 in n2.getNeighbors() and n2 in n1.getNeighbors()
            print(n1.getId()+" and "+n2.getId()+" already a neighbour.")
        else
            n1.setNeighbor(n2,distance) # n1 ----> n2
            n2.setNeighbor(n1,distance) # n2 ----> n1

            
        



        
        