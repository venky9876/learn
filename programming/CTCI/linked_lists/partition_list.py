# Wrote code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or eqal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions

from basic_ll import *

def partition_list(L, val):

    head = L

    less = less_l = ListNode()
    more = more_l = ListNode()

    while L:
        if L.key < val:
            less_l.next = L
        else:
            more_l.next = L
        L = L.next

    less_l.next = more.next

    return less.next
