# The direct implementation of an inorder traversal using recursion has O(h) space complexity, where h is the height of the tree. Recursion can be removed with an explicit stack, but the space complexity remains O(h).
# Write a nonrecursive program for computing the inorder traversal sequence for a binary tree. Assume nodes have parent fields.

### Hint : How can you tell whether a node is a left chil or right child of its parent ?

def nonrecursive_inorder(tree):

    if tree is None:
        return None
    vals  = []
    prev = None
    while tree:
        if prev is tree.parent:
            if tree.left:
                temp = tree.left
            else:
                vals.append(tree.data)
                temp = tree.right or tree.parent
        elif tree.left is prev:
            temp = tree.right or tree.parent
        else:
            temp = tree.parent

        prev, tree = tree, temp
    return vals


        

        

        

    