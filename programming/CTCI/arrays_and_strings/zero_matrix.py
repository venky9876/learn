# Write an algorithm such that if an element in an MXN matrix is 0, its entire row and column are set to 0.

def set_row_zero(M,i):

    for k in range(len(M[0])):
        M[i][k] =0
    return M

def set_col_zero(M,j):
    for k in range(len(M)):
        M[k][j] = 0

    return M

def zero_matrix(M):
    x = len(M)
    y = len(M[0])

    rows = []
    cols = []
    for i in range(x):
        for j in range(y):
            if M[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for i in rows:
        set_row_zero(M,i)
    for j in cols:
        set_col_zero(M,j)   
    
    return M

if __name__ == "__main__":

    M = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

    print (zero_matrix(M))



