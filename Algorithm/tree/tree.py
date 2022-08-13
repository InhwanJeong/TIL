class BinaryTree:
    def __init__(self, root):
        self.root = root


class Node:
    def __init__(self, value):
        self.value = value
        self.left = Node
        self.right = Node


def preorder(tree, node):
    if node != '.':
        print(tree[node]['value'], end='')
        preorder(tree, tree[node]['left'])
        preorder(tree, tree[node]['right'])


def inorder(tree, node):
    if node != '.':
        inorder(tree, tree[node]['left'])
        print(tree[node]['value'], end='')
        inorder(tree, tree[node]['right'])


def postorder(tree, node):
    if node != '.':
        postorder(tree, tree[node]['left'])
        postorder(tree, tree[node]['right'])
        print(tree[node]['value'], end='')


if __name__ == '__main__':
    tree = BinaryTree()
