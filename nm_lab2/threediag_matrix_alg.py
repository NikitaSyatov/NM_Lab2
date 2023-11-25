def Progonka(matrix_n_3,vector_b,size_n):
    Matrix = matrix_n_3
    n = size_n
    ans = vector_b

    y = []
    for i in range(n):
        y.append(0)
    a = []
    b = []
    A = []
    B = []
    C = []
    for i in range(n):
        if (i!=n-1):
            A.append(Matrix[i + 1][2])
        if (i!=0):
            B.append(Matrix[i][0])
        C.append(Matrix[i][1]*((-1)+2*(i==0)))
    C.append(1)
    a.append(0)
    a.append((-1)*B[0])
    b.append(0)
    b.append(ans[0])


    for i in range(2,n):
        a.append(B[i-1]/(C[i-1]-A[i-1]*a[i-1]))
        b.append((((-1)+2*(i-1==0))*ans[i-1]+A[i-1]*b[i-1])/(C[i-1]-A[i-1]*a[i-1]))

    y[n-1] = ((A[n-2])*b[n-1]-ans[n-1])/((-1)*A[n-2]*a[n-1] - 1)

    for i in range(n-2,-1,-1):
        y[i] = (a[i+1]*y[i+1]+b[i+1])


    return y
#1, 1, 0, 0 = 1           #1,2,3,4
#0, 1, 0, 0 = 2         #1,2,3,4
#0, 0, 1, 0 = 3
#0, 0, 0, 1 = 4
# A = [[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]
# c = [1,2,3,4]
# s = 4
# A = [[0,1,0],[0,1,0],[0,1,0],[0,1,0]]

# print(Progonka(A,c,s))
