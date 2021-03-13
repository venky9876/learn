# The successor of a node in a binary tree is the node that appears immediately after the given node in an inorder traversal.
# Design an algorithm that computes the successor of a node in a binary tree. Assume that each node stores its parent. 
### Hint : Study the node's right subtree. What if the node does not have a right subtree ?

def find_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left_size
        return node
    while node.parent and node.parent.right is node:
        node = node.parent

    return node.parent
    