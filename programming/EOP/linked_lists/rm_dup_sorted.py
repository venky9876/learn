# Write a program that takes as input a singly linked list of integers in sorted order, and removes duplicates from it. The list should be sorted.

### Hint : Focus on the successor fields which have to be updated.

def rm_dup_sorted(L):

    head = L

    s_iter = e_iter = L

    while L and L.next:
        e_iter = L.next
        if s_iter.key != e_iter.key :
            s_iter.next = e_iter
            s_iter = e_iter
        L = L.next
    return head



        
