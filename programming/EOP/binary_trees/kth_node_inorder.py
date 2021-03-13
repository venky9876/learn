# It is trivial to find the kth node that appears in an inorder traversal with O(n) time complexity, where n is the number of nodes. However, with additional information on each node, you can do better.
# Write a program that efficiently computes the kth node appearing in an inorder traversal. Assume that each node stores the number of nodes in the subtree rooted at that node.

### Hint : Use the divied and conquer principle.

def kth_node_inorder(tree, k):

    if tree is None or (tree.data < k ):
        return None
    if k == 1 or tree.left.data == k-1:
        return tree

    if tree.left.data > k :
        return kth_node_inorder(tree.left, k)
    if tree.left.data < K:
        return kth_node_inorder(tree.left, k - tree.left.data-1)


### Iteration

def find_kth_node_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < K:
            k -= left_size + 1
            tree = tree.right
        elif left_size == k-1:
            return tree
        else:
            tree = tree.left

    return None
    

    
    
