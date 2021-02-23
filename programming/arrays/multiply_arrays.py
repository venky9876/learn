# Write a program the takes two arrays representing integers, and returns an integer representing their product.

def prod_array_num(arr, num):

    prod_array = [None]*len(arr)

    carry = 0
    for i in reversed(range(arr)):
        temp_prod = arr[i]*num + carry
        if (temp_prod > 9):
            carry = temp_prod[0]
            prod_array[i] = temp_prod[1]
        else:
            prod_array[i] = temp_prod
    return prod_array



def multiply_array(a1,a2):

    if ((a1[0] < 0) ^ (a2[0] < 0)):
        sign = -1
    else:
        sign = 1

    a1[0] = abs(a1[0])
    a2[0] = abs(a2[0])

    result = [0]*(len(a1) + len(a2))
    for i in reversed(range(len(a1))):
        for j in reversed(range(len(a2))):
            result[i+j+1] += a1[i]*a2[j]
            result[i+j] += result[i+j+1]//10
            result[i+j+1] = result[i+j+1]%10
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]

    return [sign*result[0]] + result[1:]

if __name__ == "__main__":

    a1 = [1,2]
    a2 = [2,3]

    prod_array = multiply_array(a1,a2)

    print ("product of %s and %s is %s"%(a1,a2,prod_array))