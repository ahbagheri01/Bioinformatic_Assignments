import numpy as np


class Tree:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency = []

    def __repr__(self):
        return f'Tree: {self.adjacency}'

    def __len__(self):
        return len(self.nodes)

    def add_node(self, index):
        node = Node(index)
        self.nodes.append(node)
        return node

    def add_edge(self, src, dest, weight=0):
        src = self.get_node(src)
        dest = self.get_node(dest)
        edge = Edge(src, dest, weight)
        self.adjacency.append(edge)

    def get_node(self, index):
        for node in self.nodes:
            if node.index == index:
                return node
        return None

    def print(self):
        self.adjacency.sort(key=lambda e: e.src.index)
        for edge in self.adjacency:
            print(f'{edge.src.index}->{edge.dest.index}:{edge.weight:.3f}')


class Cluster:
    def __init__(self, nodes, index=-1):
        self.nodes = nodes
        self.index = index

    def __len__(self):
        return len(self.nodes)

    def __repr__(self):
        return f'Cluster {self.index}: {self.nodes}'

    def __eq__(self, other):
        return self.index == other.index


class Node:
    def __init__(self, index, age=0):
        self.index = index
        self.age = age

    def __repr__(self):
        return f'Node {self.index}: {self.age}'

    def __eq__(self, other):
        return self.index == other.index


class Edge:
    def __init__(self, src: Node, dest: Node, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f'{self.src.index}->{self.dest.index}:{self.weight}'

    def __eq__(self, other):
        return self.src == other.src and self.dest == other.dest


def cluster_distance(c_i: Cluster, c_j: Cluster):
    print(distance_matrix)
    distance = 0
    for i in range(len(c_i)):
        p = c_i.nodes[i]
        for j in range(len(c_j)):
            q = c_j.nodes[j]
            distance += distance_matrix[p.index, q.index]
    distance /= len(c_i) * len(c_j)
    return distance


def find_closest(clusters):
    min_distance = np.inf
    closest = (None, None)
    for i in range(len(clusters)):
        c_i = clusters[i]
        for j in range(i + 1, len(clusters)):
            c_j = clusters[j]
            distance = cluster_distance(c_i, c_j)
            if distance < min_distance:
                min_distance = distance
                closest = (c_i, c_j, i, j)
    return closest


def merge_cluster(c_i: Cluster, c_j: Cluster):
    new_nodes = c_i.nodes + c_j.nodes
    c_new = Cluster(new_nodes)
    return c_new


def remove_nodes(D, c_i, c_j):
    D = np.delete(D, c_i, axis=0)
    D = np.delete(D, c_i, axis=1)
    D = np.delete(D, c_j, axis=0)
    D = np.delete(D, c_j, axis=1)
    return D


def upgma(D, n):
    clusters = [Cluster([Node(i)], i) for i in range(n)]
    nodes = [Node(i) for i in range(n)]
    T = Tree(nodes)

    while len(clusters) > 1:
        # find closest clusters
        c_i, c_j, i, j = find_closest(clusters)
        # merge clusters
        c_new = merge_cluster(c_i, c_j)
        c_new.index = len(T)
        # add new node
        new_node = T.add_node(c_new.index)
        # connect new node
        T.add_edge(new_node.index, c_i.index)
        T.add_edge(c_i.index, new_node.index)
        T.add_edge(new_node.index, c_j.index)
        T.add_edge(c_j.index, new_node.index)
        # set age
        new_node.age = cluster_distance(c_i, c_j) / 2
        # remove clusters
        clusters.remove(c_i)
        clusters.remove(c_j)
        # add new row/column for new cluster
        D = np.vstack([D, np.zeros(len(D))])
        D = np.hstack([D, np.zeros((len(D), 1))])
        for i, c in enumerate(clusters):
            if c == c_i or c == c_j:
                continue
            # D[c.index, -1] = (D[c.index, c_i.index] + D[c.index, c_j.index]) / 2
            # D[-1, c.index] = (D[c.index, c_i.index] + D[c.index, c_j.index]) / 2
            D[i, -1] = cluster_distance(c, c_new)
            D[-1, i] = D[i, -1]
        # remove rows and columns
        D = remove_nodes(D, i, j)
        # add new cluster
        clusters.append(c_new)

    # root = T.get_node(clusters[0].index)
    for edge in T.adjacency:
        edge.weight = abs(edge.src.age - edge.dest.age)
    return T


if __name__ == '__main__':
    input_file = open("rosalind_ba7d.txt", "r")
    lines = input_file.readlines()
    n = int(lines[0].rstrip())
    lines = lines[1:]
    distance_matrix = np.zeros(shape=(n, n))
    for i, line in enumerate(lines):
        row_str = line.rstrip()
        distance_matrix[i] = list(map(int, row_str.split()))

    T = upgma(distance_matrix, n)
    T.print()