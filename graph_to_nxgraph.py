import networkx as nx
from graph import Digraph


class GraphToNxGraph(object):
    def __init__(self, graph):
        self.graph = graph
        self.nx_graph = nx.DiGraph()
        for node in self.graph.get_nodes():
            self.nx_graph.add_node(node.get_id(), ACT=node.get_weight())

        for node, edge_list in self.graph.edges.items():
            for edge in edge_list:
                self.nx_graph.add_edge(edge.get_source(), edge.get_destination(), {'comm': edge.get_weight()})

    def get_graph(self):
        return self.graph

    def get_nx_graph(self):
        return self.nx_graph


g = Digraph('datasets/BittencourtRizosMadeira.txt')
converter = GraphToNxGraph(g)
nx_g = converter.get_nx_graph()

print("Nodes: {}".format(nx_g.nodes()))
print("Edges: {}".format(nx_g.edges()))
