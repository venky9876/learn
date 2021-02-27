# For the pupose of this problem, define a palindromic string to be string which when all the nonalphanumerc are removed it reads the same fron to back ignoring case. For example, " A man, a plan, a canal, Panama"
# Implement a function which takes as input a string s and returns true if s is a palindromic string.

## Hint : Use two indices.


def test_palin_str(strr):

    front_ind = 0
    back_ind = len(strr) - 1
    #is_palin = False
    while(True):

        if front_ind >= back_ind:
            break

        if not str(strr[front_ind]).isalnum():
            front_ind += 1
            continue
        if not str(strr[back_ind]).isalnum():
            back_ind -= 1
            continue

        if strr[front_ind].lower() != strr[back_ind].lower():
            return False
        else:
            front_ind += 1
            back_ind -= 1

    return True

if __name__ == "__main__":

    strr = "A man, a plan, a canal, Panama. Venky"

    flag = test_palin_str(strr)

    print ("Is %s palindormic - %s"%(strr, flag))
        

            
        


