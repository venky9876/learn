# Write a program which takes a singly linked list L and two integers s and f as arguments, and reverses the order of the nodes from the sth node to fth node, inclusiive. The numbering begins at 1, i.e., the head node is the first node. Do not allocate additional nodes.

### Hint : Focuse on the successor fidles which have to be updated.

from basic_ll import *

def reverse_sublist(L, start, finish):

    dummy_head = sublist_head = ListNode(0,L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next

    for _ in range(finish - start):

        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next