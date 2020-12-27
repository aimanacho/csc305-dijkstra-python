class 
- graph 
- node


Class Node:
    
    attributes:
    - __char id
    - __neighbors
    - __shortest_dist ** default = inf
    - __prev node ** default = null


Class Graph: 

Method:

- // add_unidirectional_edges(string node1, string node2, int distance)
- // add_bidirectional_edges(string node1, string node2, int distance)
- dijkstra( string startingNode )
- shortest_path( string startingNode, string destinationNode )
- display_table( string originNode )


Application Class

Class Prob 1:
import Class Graph, Node

g = Graph()
g.add_unidirectional_edges('s', 'a', 1)
g.add_unidirectional_edges('s', 'c', 2)
g.add_unidirectional_edges('a', 'b', 6)
g.add_unidirectional_edges('c', 'a', 4)
g.add_unidirectional_edges('c', 'd', 3)
...

g.shortest_path()