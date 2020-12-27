from graph import Graph

g = Graph()

g.add_unidirectional_edges('a','b',6)
g.add_unidirectional_edges('b','e',2)
g.add_unidirectional_edges('b','d',1)
g.add_unidirectional_edges('d','e',1)
g.add_unidirectional_edges('c','a',4)
g.add_unidirectional_edges('c','d',3)
g.add_unidirectional_edges('s','a',1)
g.add_unidirectional_edges('s','c',2)


print(n)
