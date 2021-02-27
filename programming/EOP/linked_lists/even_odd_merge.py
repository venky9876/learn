# Consider a singly linked list whose nodes are numbered starting at 0. Define the even-odd merge of the list to be the list consisting of the even-numbered nodes followed by the odd-numbered nodes. Write a program the computes the even-odd merge.

### Hint : Use temporary additional storage.


def even_odd_merge(L):

    first_even = even = L
    first_odd = odd = L.next
    i = 0
    while L:
        if i % 2 == 0:
            even.next = L
            even = even.next
        else:
            odd.next = L
            odd = odd.next
        L = L.next
    even.next = first_odd

    return first_even

       

        



        






        




