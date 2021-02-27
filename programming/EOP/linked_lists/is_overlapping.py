# Write a program that takes two cycle-free singly linked lists, and determines if there exists a node that is common to both lists.

### Hint : Solve the simple cases first.

from basic_ll import *

def find_length(L):
    leng  = 0

    while L:
        leng += 1
        L = L.Next

    return leng

def is_overlapping(L1, L2):

    l1_len = find_length(L1)
    l2_len = find_length(L2)
    if l1_len > l2_len:
        long_L = L1
        short_L = L2
    else:
        long_L = L2
        short_L = L1

    for i in range(abs(l2_len - l1_len)):
        long_L = long_L.next

    while long_L and short_L is not long_L:
        long_L = long_L.next
        short_L = short_L.next

    return long_L

    




    return

