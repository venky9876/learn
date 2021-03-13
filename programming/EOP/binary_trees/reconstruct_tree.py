# Given an inorder traversal sequence and a preorder traversal sequence of a binary tree write a program to reconstruct the tree. Assume each node has a unique key.

### Hint : Focus on the root.
from binarytree import *

def reconstruct_tree(inorder, preorder):

    node_to_inorder_idx = {data: i for i , data in enumerate(inorder)}

    def reconstruct_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(preorder[preorder_start], reconstruct_helper(preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, root_inorder_idx), reconstruct_helper(preorder_start + 1 + left_subtree_size, preorder_end, root_inorder_idx + 1, inorder_end))

    return reconstruct_helper(0, len(preorder), 0, len(inorder))
    

