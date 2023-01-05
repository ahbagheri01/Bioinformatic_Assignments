import time

import numpy as np


class Tree:
    def __init__(self):
        self.nodes = {}
        self.adjacency = []

    def __repr__(self):
        return f'Tree: {self.adjacency}'

    def __len__(self):
        return len(self.nodes)

    def add_node(self, index):
        if index in self.nodes:
            return self.nodes[index]
        node = Node(index)
        self.nodes[index] = node
        return node

    def add_edge(self, src, dest, weight=0):
        edge = Edge(src, dest, weight)
        self.adjacency.append(edge)

    def get_node(self, index):
        if index in self.nodes:
            return self.nodes[index]
        return None

    def get_children(self, node):
        # children = []
        # for edge in self.adjacency:
        #     if edge.src == node:
        #         children.append(edge.dest)
        return node.children

    def get_son(self, node):
        return self.get_children(node)[0]

    def get_daughter(self, node):
        return self.get_children(node)[1]

    def is_ripe(self, node):
        return not node.is_leaf() and node.tag == 0 and \
               self.get_son(node).tag == 1 and \
               self.get_daughter(node).tag == 1

    def get_ripes(self):
        ripes = []
        for v_i, v in self.nodes.items():
            if self.is_ripe(v):
                ripes.append(v)
        return ripes

    def get_min_from_children(self, node, k, index):
        min_son, c_son = self.get_son(node).get_min_score(k, index)
        min_daughter, c_daughter = self.get_daughter(node).get_min_score(k, index)
        node.backtrack[index][k] = (c_son, c_daughter)
        return min_son + min_daughter

    def get_root_min(self, index):
        root_i, root = list(self.nodes.items())[-1]
        min_score = np.inf
        for k in alphabet:
            score = root.s[index][k]
            if score < min_score:
                min_score = score
                character[root.index][index] = k
        self.backtrack(root, index)
        return min_score

    def backtrack(self, node, index):
        # if node.is_leaf():
        #     return
        son = self.get_son(node)
        if son.is_leaf():
            return
        min_c = character[node.index][index]
        character[son.index][index] = node.backtrack[index][min_c][0]
        daughter = self.get_daughter(node)
        character[daughter.index][index] = node.backtrack[index][min_c][1]
        self.backtrack(son, index)
        self.backtrack(daughter, index)


class Node:
    def __init__(self, index):
        self.index = index
        self.children = []
        self.tag = 0
        self.s = [{}] * len_leaf_dna
        self.backtrack = [{}] * len_leaf_dna

    def get_min_score(self, k, index):
        min_val = np.inf
        min_c = None
        for c in alphabet:
            s = self.s[index][c] + (0 if c == k else 1)
            if s < min_val:
                min_val = s
                if not self.is_leaf():
                    min_c = c
                    # character[self.index][index] = c
        return min_val, min_c

    def get_dna(self):
        return ''.join(character[self.index])

    def is_leaf(self):
        return self.index < n

    def __repr__(self):
        return f'Node {self.index}: {self.get_dna()}'

    def __eq__(self, other):
        return self.index == other.index


class Edge:
    def __init__(self, src: Node, dest: Node, weight=0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f'{self.src.index}->{self.dest.index}'

    def __eq__(self, other):
        return self.src == other.src and self.dest == other.dest


def hamming_distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance


def small_parsimony(T, character, index):
    for v_i, v in T.nodes.items():
        v.tag = 0
        if v.is_leaf():
            v.tag = 1
            for k in alphabet:
                if character[v_i][index] == k:
                    v.s[index][k] = 0
                else:
                    v.s[index][k] = np.inf
    ripes = T.get_ripes()
    while ripes:
        v = ripes[0]
        v.tag = 1
        for k in alphabet:
            v.s[index][k] = T.get_min_from_children(v, k, index)
        ripes = T.get_ripes()
    return T.get_root_min(index)


if __name__ == '__main__':
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    n = int(lines[0].rstrip())
    lines = lines[1:]
    T = Tree()
    alphabet = ['A', 'C', 'T', 'G']
    character = {}
    leafs = 0
    len_leaf_dna = 0
    for line in lines:
        nodes = line.rstrip().split('->')
        if nodes[1].isdigit():
            # mid edge
            src, dest = int(nodes[0]), int(nodes[1])
            character[src] = [''] * len_leaf_dna
            character[dest] = [''] * len_leaf_dna
            src = T.add_node(src)
            dest = T.add_node(dest)
            src.children.append(dest)
            T.add_edge(src, dest)
            T.add_edge(dest, src)
        else:
            # leaf edge
            src, dest = int(nodes[0]), leafs
            leafs += 1
            len_leaf_dna = len(nodes[1])
            character[src] = [''] * len_leaf_dna
            character[dest] = nodes[1]
            src = T.add_node(src)
            dest = T.add_node(dest)
            src.children.append(dest)
            T.add_edge(src, dest)
            T.add_edge(dest, src)

    T.nodes = dict(sorted(T.nodes.items()))

    score = 0
    for i in range(len_leaf_dna):
        score += small_parsimony(T, character, i)

    with open('output.txt', 'w') as file:
        file.write(f'{score}\n')
        for edge in T.adjacency:
            src_dna = edge.src.get_dna()
            dest_dna = edge.dest.get_dna()
            file.write(f'{src_dna}->{dest_dna}:{hamming_distance(src_dna, dest_dna)}\n')
    # print(score)
    # for edge in T.adjacency:
    #     src_dna = edge.src.get_dna()
    #     dest_dna = edge.dest.get_dna()
    #     print(f'{src_dna}->{dest_dna}:{hamming_distance(src_dna, dest_dna)}')