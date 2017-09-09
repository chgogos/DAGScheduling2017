import pytest

from graph import *

'''
see:
1) https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
for testing Python Applications with Pytest

2) http://gowrishankarnath.com/using-pytest-testing-tool-to-test-python-code-by-configuring-pycharm-ide/
for configuring pycharm in order to run pytest tests

'''


@pytest.fixture
def simple_graph():
    """Returns a simple graph"""
    g = Digraph()
    node_list = [('T1', [3]), ('T2', [7]), ('T3', [4]), ('T4', [2]), ('T5', [6]), ('T6', [4]), ('T7', [2])]
    for (n, w) in node_list:
        g.add_node(Node(n, w))
    edge_list = [('T1', 'T3', 1), ('T1', 'T4', 5), ('T1', 'T5', 6), ('T3', 'T6', 7), ('T4', 'T2', 4), ('T5', 'T2', 2),
                 ('T6', 'T7', 8), ('T2', 'T7', 3)]
    for (n1, n2, w) in edge_list:
        g.add_edge(Edge(n1, n2, w))
    return g


def test_simple_graph(simple_graph):
    assert simple_graph.get_number_of_nodes() == 7
    assert simple_graph.get_number_of_edges() == 8


@pytest.mark.parametrize("filename,number_of_nodes,number_of_edges", [
    ('datasets\BittencourtRizosMadeira.txt', 9, 14),
    ('datasets\Prashanth_dissertation_page19.txt', 10, 15),
    ('datasets\SakellariouZhao.txt', 10, 14),
    ('datasets\Sinnen_page81.txt', 11, 14),
    ('datasets\Sinnen_page142.txt', 12, 17),
    ('datasets\TopcuoglouHaririWu2002.txt', 10, 15)
])
def test_load_graphs_from_disk(filename, number_of_nodes, number_of_edges):
    g = Digraph(filename)
    assert g.get_number_of_nodes() == number_of_nodes
    assert g.get_number_of_edges() == number_of_edges
