# Write a program which takes two singly linked lists of digits, and returns the list corresponding to the sum of the integers they represent. The least significant digit comes first.

### Hint : First, solve the problem assuming no pair of corresponding digits sum to more than 9
from basic_ll import *


def add_two_numbers(L1, L2):

    L_sum = ListNode()
    carry = 0
    while L1 and L2:

        L_sum.key = (L1.key + L2.key)%10 + carry
        carry = (L1.key + L2. key)//10

        temp = ListNode()

        L_sum.next = temp
        L_sum = L_sum.next

        L1 = L1.next

        L2 = L2.next

    L_temp = L1 or L2

    while L_temp:
        L_sum.key = (L_temp.key + carry)%10 + carry
        carry = (L_temp.key)//10

        temp = ListNode()
        L_sum.next = temp
        L_sum = L_sum.next

        L_temp = L_temp.next

    return L_sum
    

