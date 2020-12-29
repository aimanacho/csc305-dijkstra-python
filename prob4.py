from graph import Graph

g = Graph()

g.add_unidirectional_edges('a','c',5)
g.add_unidirectional_edges('a','b',3)
g.add_unidirectional_edges('f','a',3)
g.add_unidirectional_edges('f','d',7)
g.add_unidirectional_edges('b','c',2)
g.add_unidirectional_edges('b','d',6)
g.add_unidirectional_edges('c','b',1)
g.add_unidirectional_edges('c','d',4)
g.add_unidirectional_edges('c','f',6)
g.add_unidirectional_edges('d','f',3)

g.shortest_path('a', 'd')

