# Simple iterative binary search

def bsearch(t,A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L)/2
        if A[M] < t:
            L = M + 1
        if A[M] == t:
            return M
        else:
            U = M - 1
    return None

    