#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def count_leafs( top ):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    else:
        return count_leafs( top.left ) + count_leafs( top.right )

def count_total( top ):
    if top is None:
        return 0
    return top.data + count_total( top.left ) + count_total( top.right )

tree = Tree(1)
tree.left = Tree(1)
tree.right = Tree(1)
tree.left.left = Tree(1)
tree.left.right = Tree(1)
tree.left.left.left = Tree(1)
tree.left.left.right = Tree(1)
tree.right.right = Tree(1)
tree.right.right.right = Tree(1)

print("Count_total: " + str(count_total(tree)))
print("Count_leafs: " + str(count_leafs(tree)))