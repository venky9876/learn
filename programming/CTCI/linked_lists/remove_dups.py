# Write code to remove duplicates from an unsorted linked list.

from basic_ll import *

from collections import Counter

def remove_dups(L):

    if not L or not L.next:
        return L
    
    unique_set = set()

    head = L
    unique_set.add(L.key)
    while not L.next:
        if L.next.key not in unique_set:
            unique_set.add(L.next.key)
            L = L.next
        else:
            L.next = L.next.next
    return head


            
            

