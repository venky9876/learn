# Implement an algorithm that takesas input an array of distinct elements and a size, and returns a subset of the given size of the array elements. All subsets should be equally likely. Return the result in input array itself.

# NEED REVIEW

import random

def random_sampling(k,A):
    for i in range(k):
        r = random.randint(i,len(A)-1)
        A[i], A[r] = A[r], A[i]

