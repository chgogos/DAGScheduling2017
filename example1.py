import networkx as nx
import platform
from networkx.drawing.nx_agraph import write_dot
from collections import namedtuple

""" 
Manual creation of a graph using library networkx 

Journal of Supercomputing
Granularity-based workflow scheduling algorithm for cloud computing
Mahdu Sudan Kumar et. al. (2017) - Figure 1
"""

DG = nx.DiGraph()
nodes = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7']
weights = [3, 7, 4, 2, 6, 4, 2]
CommEdge = namedtuple('CommEdge', 'from_n to_n weight')
edges = [CommEdge('T1', 'T3', 1), CommEdge('T1', 'T4', 5), CommEdge('T1', 'T5', 6), CommEdge('T3', 'T6', 7),
         CommEdge('T4', 'T2', 4), CommEdge('T5', 'T2', 2), CommEdge('T6', 'T7', 8), CommEdge('T2', 'T7', 3)]

for i, n in enumerate(nodes):
    DG.add_node(n, ACT=weights[i])

for e in edges:
    DG.add_edge(e.from_n, e.to_n, {'comm': e.weight})

if platform.system() != 'Windows':
    write_dot(DG, "tmp\wf1.dot")

ts = nx.topological_sort(DG)
print("Topological sort: " + str(ts))
