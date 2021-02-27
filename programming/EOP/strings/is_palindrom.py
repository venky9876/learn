
def is_palindrom(strr):
    for i in range(len(strr)//2):
        if strr[i] != strr[~i]:
            return False

    return True

if __name__ == "__main__":

    strr = "venkyyknev"

    flag = is_palindrom(strr)
    print ("Is %s a palindorme - %s"%(strr, flag))