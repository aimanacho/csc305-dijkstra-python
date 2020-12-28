from graph import Graph

g = Graph()

g.add_unidirectional_edges('a','e',7)
g.add_unidirectional_edges('b','a',4)
g.add_unidirectional_edges('c','b',1)
g.add_unidirectional_edges('d','b',2)
g.add_unidirectional_edges('d','c',6)