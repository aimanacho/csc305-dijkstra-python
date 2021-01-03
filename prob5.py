from graph import Graph

g = Graph()

g.add_unidirectional_edges('a','b',4)
g.add_unidirectional_edges('a','c',2)
g.add_unidirectional_edges('b','c',5)
g.add_unidirectional_edges('b','d',10)
g.add_unidirectional_edges('c','e',3)
g.add_unidirectional_edges('d','f',11)
g.add_unidirectional_edges('e','d',4)


g.shortest_path('a', 'f')
