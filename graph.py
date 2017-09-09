from random import shuffle
from collections import deque
from statistics import mean


class Node:
    def __init__(self, id, execution_times_per_processor):
        self.id = id
        self.execution_times_per_processor = execution_times_per_processor

    def get_id(self):
        return self.id

    def get_execution_times_per_processor(self):
        return self.execution_times_per_processor

    def get_weight(self):
        return mean(self.execution_times_per_processor)

    def __str__(self):
        return self.id + ' ' + str(self.execution_times_per_processor) + \
               ' avg:(' + '{0:.2f}'.format(self.get_weight()) + ')'


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.source + '-(' + str(self.weight) + ')->' + self.destination


class Digraph:
    def __init__(self, filename=None):
        self.nodes = []
        self.edges = {}
        if filename is not None:
            tasks = 0
            edges = 0
            section = ''
            with open(filename) as f:
                c = 0
                for line in f:
                    if line[0] == '#':
                        continue
                    if 'Tasks' in line:
                        tasks = int(line.split(':')[1])
                        section = 'Tasks'
                    elif 'Dependencies' in line:
                        edges = int(line.split(':')[1])
                        section = 'Dependencies'
                    else:
                        if section == 'Tasks':
                            node_list = line.split()
                            self.add_node(Node(node_list[0], [float(x) for x in node_list[1:]]))
                        if section == 'Dependencies':
                            c += 1
                            edge_list = line.split()
                            self.add_edge(Edge(edge_list[0], edge_list[1], float(edge_list[2])))
            if tasks != len(self.nodes) or edges != c:
                raise ValueError("Wrong number of tasks")
            if edges != c:
                raise ValueError("Wrong number of edges")

    def get_nodes(self):
        return self.nodes

    def get_number_of_nodes(self):
        return len(self.nodes)

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Node already exists')
        else:
            self.nodes.append(node)
            self.edges[node.get_id()] = []

    def add_edge(self, edge):
        source = edge.get_source()
        destination = edge.get_destination()
        if not (source in [x.get_id() for x in self.nodes] and destination in [x.get_id() for x in self.nodes]):
            raise ValueError('Node does not exist in the graph')
        self.edges[source].append(edge)

    def get_number_of_edges(self):
        c = 0
        for node in self.edges:
            c += len(self.edges[node])
        return c

    def children_of(self, node_id):
        children = [edge.get_destination() for edge in self.edges[node_id]]
        children.sort()
        return children

    def depth_first_search(self, start, end, randomize=False):
        visited = set()
        stack = deque([(start, [start])])
        while stack:
            (current, path) = stack.pop()
            if current == end:
                return path
            if current not in visited:
                visited.add(current)
                children = self.children_of(current)
                if randomize:
                    shuffle(children)
                stack.extendleft([(node, path + [node]) for node in children])
        return None

    def find_shortest_path(self, start, end, path, shortest):
        path = path + [start]
        if start == end:
            return path
        for node in self.children_of(start):
            if node not in path:
                if shortest is None or len(path) < len(shortest):
                    new_path = self.find_shortest_path(node, end, path, shortest)
                    if new_path is not None:
                        shortest = new_path
        return shortest

    def shortest_path(self, start, end):
        return self.find_shortest_path(start, end, [], None)

    def __str__(self):
        result = ''
        for node in self.nodes:
            result += str(node) + ':  '
            for edge in self.edges[node.get_id()]:
                result += ' ' + str(edge) + ', '
            result = result[:-2]
            result += '\n'
        return result
