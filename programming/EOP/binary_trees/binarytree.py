# Basic binary tree node.

class BinaryTreeNode:

    def __init__(self, data = None, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right

        return


def tree_traversal(root):

    if root :
        print ('Preorder : %d'% root.data)
        tree_traversal(root.left)
        print ('Inorder: %d'%root.data)
        tree_traversal(root.left)
        print ('Postorder : %d'%root.data)

    
