# Implement an integer to string conversion function, and a string to integer conversion function. For example, if the input to the first function is the integer 314, it should return the string "314" and if the input to the second function is the string "314" it should return the integer 314.

def str_to_int(strr):
    intt = 0
    flag = 0
    if strr[0] == '-':
        flag = 1
    for i in range(flag, len(strr)):
        intt = 10*intt + int(strr[i])
    if flag:
        return -1*intt
    return intt

def int_to_str(intt):

    is_neg = False
    if intt < 0:
        is_neg = True
    str_list = []
    while True:
        str_list.append(str(intt%10))
        intt //= 10
        if intt == 0:
            break

    return ('-' if is_neg else '') + ''.join(reversed(str_list))

    return



if __name__ == "__main__":

    strr = "-1234"

    intt = str_to_int(strr)

    print (str(intt) + " type - " + str(type(intt)))
