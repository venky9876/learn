# Given a binary tree, compute a linked list from the leaves of the binary tree. The leaves should appear in left-to-right order.
### Hint : Build the list incrementally - it's easy if the partial list is a global.

leaves_list = []

def build_linked_list(tree):

    if tree is None:
        return []
    if tree.left is None and tree.right is None:
        leaves_list.append(tree.data)
    elif tree.left is not None:
        build_linked_list(tree.left)
    else:
        build_linked_list(tree.right)


    

