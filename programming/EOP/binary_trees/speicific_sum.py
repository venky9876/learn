# You are given a binary tree where each node is labeled with an integer. The path weight of a node in such a tree is the sum of the integers on the unique path from the root to that node. 
# Write a program which takes as input an integer and a binary tree with integer node weights, and checks if there exists a leaf whose path weight equals the given integer.

### Hint : What do you need to know about the rest of the tree when checking a specific subtree

def is_specific_sum(tree, checksum):

    if tree is None and checksum != 0 :
        return False
    if tree is None and checksum == 0:
        return True
    
    
    if tree.data > checksum:
        return False
    else:

        return (is_specific_sum(tree.left, checksum - tree.data) or is_specific_sum(tree.right, checksum - tree.data))

