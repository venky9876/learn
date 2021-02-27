# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. Yor are required to solved it without allocating additional space

def even_odd(A):

    next_even, next_odd = 0, len(A)-1

    while next_even < next_odd:
        if A[next_even] % 2 != 0:
            temp = A[next_odd]
            A[next_odd] = A[next_even]
            A[next_even]= temp
            next_odd -= 1
        else :
            next_even += 1
    
    return A
    

if __name__ == "__main__":

    A = [3,4,6,2,7,9,3, 45, 68, 89]
    org_A = A.copy()
    reordered_A = even_odd(A)
    print ("Original list : %s"%(org_A))
    print ("Reordered list : %s"%(reordered_A))


