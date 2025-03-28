import sys


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
    n = int(sys.stdin.readline().replace("\n", ""))
    input_list = [sys.stdin.readline().replace("\n", "").split() for _ in range(n)]
    tree = {
            item[0]:
                     {
                          'value': item[0],
                          'left': item[1],
                          'right': item[2],
                        }
                 for item in input_list
    }

    root = input_list[0][0]

    preorder(tree, root)
    print()
    inorder(tree, root)
    print()
    postorder(tree, root)
