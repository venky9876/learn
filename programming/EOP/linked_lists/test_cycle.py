# Write a program that takes that head of singly linked list and return null if there does not exist a cycle, and the node at that start of the cycle, if a  cycle is present. (You do not know the length of the list in advance)

## Hint : Consider using two iteratiors, one fast and one slow.
from basic_ll import *

def cycle_len(cycle_node):

    start, leng = cycle_node, 0

    while True:
        leng += 1
        cycle_node = cycle_node.next
        if start == cycle_node:
            return leng

def is_cycle(L):

    head = ListNode(0, L)

    sc = L
    bc = L
    cycle_flag = False
    while bc and bc.next and bc.next.next:

        sc = sc.next
        bc = bc.next.next

        if sc == bc:
            cycle_flag = True
            
            circum = cycle_len(bc)

            adv_itr = L
            for _ in range(circum):
                adv_itr = adv_itr.next

            fol_itr = L

            while fol_itr is not adv_itr:
                fol_itr = fol_itr.next
                adv_itr = adv_itr.next
            return fol_itr

    return None
    
    
    return cycle_flag




