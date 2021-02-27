# Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field your program can change in a node is its next field.

### Hint : Two sorted arrays can be merged using two indicces. For lists, take care when one iterator reaches the end.

from basic_ll import *

def merge_two_sorted_lists(L1, L2):

    final = temp = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            temp.next, L1 = L1, L1.next
        else:
            temp.next, L2 = L2, L2.Next

    temp.next = L1 or L2

    return final.next

    











