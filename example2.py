from graph import Digraph, Node, Edge

""" 
Manual creation of a graph
"""


g = Digraph()
node_list = [('T1', [3]), ('T2', [7]), ('T3', [4]), ('T4', [2]), ('T5', [6]), ('T6', [4]), ('T7', [2])]
for (n, w) in node_list:
    g.add_node(Node(n, w))

edge_list = [('T1', 'T3', 1), ('T1', 'T4', 5), ('T1', 'T5', 6), ('T3', 'T6', 7), ('T4', 'T2', 4), ('T5', 'T2', 2),
             ('T6', 'T7', 8), ('T2', 'T7', 3)]
for (n1, n2, w) in edge_list:
    g.add_edge(Edge(n1, n2, w))

print("Graph info")
print(g)
print("#nodes={} #edges={}".format(g.get_number_of_nodes(), g.get_number_of_edges()))

print('Shortest path')
print(g.shortest_path('T1', 'T7'))

print('DFS choosing randomly among children')
print(g.depth_first_search('T1', 'T7', True))
