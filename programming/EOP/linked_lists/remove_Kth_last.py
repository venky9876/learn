# Given a singly linked list and an integer k, write a program to remove the kth last element from the list. Your algorithm cannot use more than a few words of storage, regardless of the length of the list. In particular, you cannot resume that it is possible to record the length of the list.

### Hint : If you know the length of the list, can you find the kth last node using two iterators ?

def del_element(L, k):

    head = L_iter = L

    for _ range(K + 1):

        L_iter = L_iter.next

    while L_iter :

        L = L.Next
        L_iter = L_iter.Next

    L.next = L.next.next

    return head

    

    

    