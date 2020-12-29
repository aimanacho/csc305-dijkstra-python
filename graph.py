from node import Node
from math import inf

class Graph:

    def __init__(self):
        self.__node = []

    #node1 = origin, node2 = destination
    def add_unidirectional_edges(self, from_node_id, to_node_id, distance):
        #ensure from_node_id and start_node_id is not the same
        if from_node_id == to_node_id:
            print("Cannot insert same node")
            return
        
        # 1. declare two variable nodes
        n1 = n2 = None
        
        # 2. check if exist
        for x in self.__node:
            if x.getId()==from_node_id:
                n1 = x
            if x.getId()==to_node_id:
                n2 = x

        # 3. if n1 or n2 is None, create from_node_id / to_node_id
        if n1 is None:
            n1 = Node(from_node_id)
            self.__node.append(n1)
        
        if n2 is None:
            n2 = Node(to_node_id)
            self.__node.append(n2)

        # add neighbour
        if n1 in n2.getNeighbors() and n2 in n1.getNeighbors():
            print("Is already neighbours")
        else:
            n1.setNeighbor(n2,distance) # n1 ----> n2


    
    def add_bidirectional_edges( self, node1, node2, distance):
        #ensure from_node_id and start_node_id is not the same
        if node1 == node2:
            print("Cannot insert same node")
            return

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
           self.__node.append(n1)
        if n2 is None:
            n2 = Node(node2)
            self.__node.append(n2)

        #Set neighbour between edges
        #Check if 2 edges oredi a neihbor exist
        if n1 in n2.getNeighbors() and n2 in n1.getNeighbors():
            print(n1.getId()+" and "+n2.getId()+" already a neighbour.")
        else:
            n1.setNeighbor(n2,distance) # n1 ----> n2
            n2.setNeighbor(n1,distance) # n2 ----> n1

    def displayNode(self):
        for x in self.__node:
            print(x)

    def __display_table(self, start_node):
        print("\n\n------------------------------------Table------------------------------------------")
        print("Vertex\t\t|\tShortest Dist from vertex "+start_node.getId()+"\t|\tPrevious vertex")
        
        temp = sorted(self.__node, key=lambda x: x.getShortestDist())
        for node in temp:
            prev_node_id = node.getPrevNode().getId() if node.getPrevNode() != None else '-'
            print( node.getId()+"\t\t|\t\t\t"+str(node.getShortestDist())+"\t\t|\t\t"+ prev_node_id)

        # print("\nTable of Dijsktra's Shortest Path Algorithm")
        # print("-------------------------------------------\n")
        # print("vertex\t|\tshortest distance from vertex '"+start_node.getId().upper()+"'\t|\tprevious vertex")
        # print("-----------------------------------------------------------------------------------")

        
        # for n in temp:
        #     print(n.getId() + "\t|\t\t\t" + str(n.getShortestDist()) + "\t\t\t|\t\t" + (n.getPrevNode().getId() if n.getPrevNode() != None else "-"))
            

    def shortest_path(self, start_node_id, end_node_id):
        # validate whether both node id exist 
        start_node = None
        end_node = None
        
        # for loop to convert id to obj --> can be used for passing param in dijkstra method
        for x in self.__node:
            if x.getId() == start_node_id:
                start_node = x
            if x.getId() == end_node_id:
                end_node = x
                
        #validate if the id exists
        if start_node == None or end_node == None:
            print("The ID does not exist")
            return

        # execute dikstra method
        self.__dikjstra(start_node)

        output_node = [end_node.getId()]
        temp_end_node = end_node # to be used to display shortest distance from start node

        while end_node.getId() != start_node.getId():
            end_node = end_node.getPrevNode()
            output_node.insert(0,end_node.getId())

        print("Shortest Path: ")

        # shortest path
        for node in output_node:
            if node == end_node_id:
                print(node, end="")
                break 

            print(node+' -> ', end="")
        
        # shortest distance
        print ('\nShortest distance to '+ temp_end_node.getId() + ' = ' + str(temp_end_node.getShortestDist()) )


        #display table
        self.__display_table(start_node)

    def __dikjstra(self, start_node):
        visited = []
        unvisited = [x for x in self.__node]
        shortest_dist_from_start_node = 0
        current_node = start_node

        current_node.setShortestDist(shortest_dist_from_start_node)

        while current_node:
            #check unvisited neighbor
            for neighbor_node, distance in current_node.getNeighbors().items():
                #print(neighbor_node.getId(), distance) troubleshoot je ni
                if neighbor_node in visited:
                    continue

                #add up shortest_dist_from_start_node with distance from neighbor distance
                calc_dist = shortest_dist_from_start_node +  distance

                if calc_dist < neighbor_node.getShortestDist():
                    neighbor_node.setShortestDist(calc_dist)
                    neighbor_node.setPrevNode(current_node)

            # add current node to visited array
            visited.append(current_node)
            
            #update next node and next shortest distance
            next_shortest_dist_from_start_node = inf
            next_node = None

            for unvisited_node in unvisited:
                if unvisited_node in visited:
                    continue

                if unvisited_node.getShortestDist() < next_shortest_dist_from_start_node:
                    next_shortest_dist_from_start_node = unvisited_node.getShortestDist()
                    next_node = unvisited_node

            # update current node and shortest distance from start vertex
            if next_node:
                # finalised
                current_node = next_node
                shortest_dist_from_start_node = next_shortest_dist_from_start_node
            else: #if there are left over unvisited node
                for v in unvisited:
                    if v not in visited:
                        current_node = v
                    else:
                        current_node = None