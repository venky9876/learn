# Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array B having the property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= ...

def rearrange(A):
    for i in range(len(A)):
        A[i : i+2] = sorted(A[i : i+2], reverse = i % 2)

    return A

if __name__ == "__main__":

    A = [1,2,3,4,5,6]

    A = rearrange(A)

    print (A)    
