# Write a program which takes a input a binary tree and performs an inorder traversal of the tree. Do not use recursion. Nodes do not contain parent references.

### Hint : Simulate the function call stack

def inorder_traversal(tree):

    s, result = [], []

    while s or tree:

        if tree:
            s.append(tree)
            tree = tree.left

        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result

    