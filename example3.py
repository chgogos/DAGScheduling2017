from graph import Digraph, Node, Edge

""" 
Load a graph from a file 
"""

g = Digraph('datasets/BittencourtRizosMadeira.txt')

print("Graph info")
print(g)
print("#nodes={} #edges={}".format(g.get_number_of_nodes(), g.get_number_of_edges()))

task_start = g.get_nodes()[0].get_id()
task_finish = g.get_nodes()[-1].get_id()

print('Shortest path {}->{}'.format(task_start, task_finish))
print(g.shortest_path(task_start, task_finish))

print('DFS {}-->{} deterministic'.format(task_start, task_finish))
print(g.depth_first_search(task_start, task_finish))

print('DFS {}-->{} choosing randomly among children'.format(task_start, task_finish))
print(g.depth_first_search(task_start, task_finish, True))
