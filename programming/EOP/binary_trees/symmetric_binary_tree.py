# A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is the mirror image of the right subtree. 
# Write a program that checks whether a binary tree is symmetric.

### Hint : The definition of symmetry is recursive.

#from binarytree import *

def is_recursive(tree):

    if tree is None:
        return None
#    if tree.left is None or tree.right is None:
#        return False
    
#    if tree.left.value != tree.right.value:
#        return False

    def match_trees(tree1, tree2):

        if tree1 is None ^ tree2 is None:
            return False

        if tree1.value != tree2.value:
            return False
        
        if match_trees(tree1.left, tree2.right) and match_trees(tree1.right, tree2.left):
            return True
        else:
            return False
    
    return match_trees(tree.left, tree.right)

