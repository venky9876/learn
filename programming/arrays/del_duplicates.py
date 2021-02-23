# Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements. 

def del_duplicates(arr):
    if not arr:
        return 0

    index = 1
    for i in range(1, len(arr)):
        if (arr[index-1])!= arr[i]:
            a[index] = arr[i]
            index += 1
    return index

if __name__ == "__main__":

    a = [1,2,2,3]
    index = del_duplicates(a)

    print ("index is %s"%(index))

    