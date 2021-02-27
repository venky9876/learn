# For any integer k, the pivot of a list of integers with respect to k is that list with its nodes reordered so that all nodes containing keys less than k appear before nodes containing k, and all nodes containing keys greater than k appear after the nodes containing k.
# Implement a function which takes as input a singly linked list and an integer k and performs a pivot of the list with respect to k. The relative ordering of nodes that appear before k, and after k, must remain unchanged; the sam emusst hold for nodes holding keys equal to k.

### Hint : Form the three reginons independently.
from basic_ll import *

def list_pivot(L,k):

    #head = L
    small = small_iter = ListNode()
    same = same_iter = ListNode()
    big = big_iter = ListNode()

    while L:
        if L.key < k:
            small_iter.next = L
            small_iter = small_iter.next
        elif L.key == k:
            same_iter.next = L
            same_iter = same_iter.next
        elif L.key > k:
            big_iter.next = L
            big_iter = big_iter.next

    small_iter.next = same
    same_iter.next = big

    return small.next



        
