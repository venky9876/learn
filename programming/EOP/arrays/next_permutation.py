# Write a program that takes as input a permutation, and returns the next permutation under dictionary ordering. If the permutation is the last permutation, return the empty array. For example, if the input is [1,0,3,2] your function should return [1,2,0,3]. If the input is [3,2,1,0], return [].

def next_permutation(arr):

    if not arr:
        return []
    pivot  = len(arr)-1
    for i in reversed(range(1,len(arr))):
        #print (i)
        if arr[i-1] < arr[i]:
            pivot = i-1
            break
    
    exchange = len(arr)-1
    for j in reversed(range(pivot+1,len(arr))):
        if arr[j] > arr[pivot]:
            exchange = j
            break
    
    arr[pivot], arr[exchange] = arr[exchange], arr[pivot]
    print (pivot)
    for k in range(pivot+1, pivot+1 + int((len(arr)-pivot+1)/2)):
        print (k)
        arr[k], arr[len(arr)-k+pivot] = arr[len(arr)-k+pivot], arr[k]

    return arr

if __name__ == "__main__":

    arr = [1,2,0,4,3,0]

    next_arr = next_permutation(arr)

    print ("Next permutation is %s"%next_arr)

