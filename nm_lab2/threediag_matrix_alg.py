def Progonka(matrix_n_3,vector_b):
    input_A = matrix_n_3
    Matrix = []
    n = len(vector_b)
    print(n)
    Matrix.append([0, input_A[0][0], input_A[1][0]])
    Matrix.append([0, input_A[1][1], input_A[2][0]])
    for i in range(2, n-2):
        # print(i)
        Matrix.append([input_A[i-1][2], input_A[i][1], input_A[i+1][0]])
    Matrix.append([input_A[-2][-1], input_A[-3][-2], 0])
    Matrix.append([input_A[-2][-1], 1, 0])

    print(Matrix)
    
    sn = n-1
    ans = vector_b

    y = []
    for i in range(n):
        y.append(0)
    a = []
    b = []
    A = []
    B = []
    C = []

    mu1 = ans[0]
    mu2 = ans[sn]

    hi1 = Matrix[1][0]*(-1.0)
    hi2 = Matrix[sn-1][2]*(-1.0)

    A.append(0)
    B.append(0)
    C.append(0)

    for i in range(0,sn-1):
        A.append(Matrix[i][2])

    for i in range(1,sn):
        C.append(Matrix[i][1]*(-1))


    for i in range(2,n):
        B.append(Matrix[i][0])

    for i in range(0,n):
        a.append(0)
        b.append(0)
    # print("A = ", A)
    # print("B = ", B)
    # print("C = ", C)
    # print("a = ", a)
    # print("b = ", b)

    a[1] = hi1
    b[1] = mu1

    for i in range(1,n-1):
        a[i+1] = B[i]/(C[i]-A[i]*a[i])
        b[i+1] = ((-1)*ans[i]+A[i]*b[i])/(C[i]-A[i]*a[i])

    y[n-1] = ((-1)*hi2*b[sn]-mu2)/(hi2*a[sn]-1.0)

    for i in range(n-2,-1,-1):

        y[i] = a[i+1]*y[i+1]+b[i+1]

    return y

# c = [0,0,0,0]
# A = [[],[],[],[]]
# A[0] = [1, -1, 0, 0]; c[0] = -1
# A[1] = [2, 1, 2, 0]; c[1] = 10
# A[2] = [0, -1, 1, -5]; c[2] = -19
# A[3] = [0, 0, 2, 1]; c[3] = 10


# A[0] = [0,1,2]; c[0] = -1
# A[1] = [-1,1,-1]; c[1] = 10
# A[2] = [2,1,2]; c[2] = -19
# A[3] = [-5,1,0]; c[3] = 10

s = 4
# P = ""
# for i in range(0,s):
#     k = 0
#     for j in range(0,s):
#         P+=(f" + "*((j!=0 and k!=0) and A[i][j]>=0)+f"{A[i][j]}"*(A[i][j]!=1 and A[i][j]!=-1)+"-"*((A[i][j]==-1))+f"y{j}")*(A[i][j]!=0)
#         k+=(A[i][j]!=0)
#     P+=f" = {c[i]}\n"
# print(P)



# print("Answer",Progonka(A,c,s))