# A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete binary tree. A height-balanced binary  tree does not have to be perfect or complete.
# Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced.

### Hint : Think of a classic binary tree algorith.
import collections

def is_balanced_binary_tree(tree):

    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        left_result = check_balanced(tree.left)

        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        right_result = check_balanced(tree.right)

        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)


        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    return check_balanced(tree).balanced