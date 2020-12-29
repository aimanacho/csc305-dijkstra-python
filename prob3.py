from graph import Graph

g = Graph()

g.add_bidirectional_edges('a','b',3)
g.add_bidirectional_edges('a','c',5)
g.add_bidirectional_edges('b','c',3)
g.add_bidirectional_edges('b','d',4)
g.add_bidirectional_edges('b','e',7)
g.add_bidirectional_edges('c','e',6)
g.add_bidirectional_edges('d','f',2)
g.add_bidirectional_edges('d','e',2)
g.add_bidirectional_edges('e','f',5)

g.shortest_path('a', 'e')