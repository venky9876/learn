# Write a program that takes as input a singly linked list and a nonnegative integer k, and returns the list cyclically shifter to the right by k. 

### How does this problem differ from rotating an array ?

def cyclic_right_shift(L, k):

    head = start_iter =  end_iter = L

    for _ in range(K):

        end_iter = end_iter.next

    while end_iter.next:

        start_iter, end_iter = start_iter.next, end_iter.next

    start_iter.next = None
    end_iter.next = head

    return head

    