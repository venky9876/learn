# Any two nodes in a binary tree have a common ancestor, namely the root. The lowest common ancestor(LCA) of any two nodes in a binary tree is the node furthest from the root that is an ancestor of both nodes.
# Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not have a parent field.

### Hint : When is the root the LCA ?
import collections

def lca(tree, node1, node2):

    if tree is None:
        return None
    if node1 is None or node2 is None:
        return False

    def is_node_tree(tree, node):
        if tree is node:
            return True
        if tree is None:
            return False
        return is_node_tree(tree.left, node) or is_node_tree(tree.right, node)

    if is_node_tree(tree.left, node1):
        node1_tree = tree.left
    else:
        node2_tree = tree.right
    
    if is_node_tree(tree.left, node2):
        node2_tree = tree.left
    else:
        node2_tree = tree.right

    if node1_tree is not node2_tree:
        return tree
    else:
        return (lca(node1_tree, node1, node2))


def lca_better(tree, node0, node1):

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0,None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result
        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes + int(tree is node0) + int(tree is node1))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor