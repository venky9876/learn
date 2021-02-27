# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additonal characters, and that you are given the "true" length of the string.

def urlify(strr, length):

    if len(strr) == 0:
        return strr
    if not strr:
        return None

    index_iter = len(strr)
    strr = list(strr)

    for i in reversed(range(length)):
        if strr[i] == ' ':
            strr[index_iter-3:index_iter] = '%20'
            index_iter -= 3
        else:
            strr[index_iter-1] = strr[i]
            index_iter -= 1

    return ''.join(strr)

if __name__ == "__main__":

    strr = "I am venky    "

    print (urlify(strr, 10))


