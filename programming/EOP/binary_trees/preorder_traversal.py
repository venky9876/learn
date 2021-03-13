# Write a program which takes as input a binary tree and performs a preorder traversal of the tree. Do not use recusion. Nodes do not contain parent references.

def preorder_traversal(tree):
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result

    