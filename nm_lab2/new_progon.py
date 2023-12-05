def Progonka(matrix_A, vector_b):
    size = len(vector_b)
    y = []
    alpha = []
    betta = []
    alpha.append(0.)
    betta.append(vector_b[0])
    for i in range(1, size-1):
        alpha.append(matrix_A[i][2]/(-matrix_A[i][1] - matrix_A[i][0]*alpha[i-1]))
        betta.append((-vector_b[i] + matrix_A[i][0]*betta[i-1])/(-matrix_A[i][1]) - matrix_A[i][0]*alpha[i-1])

    print(alpha)
    print(betta)

    y.append(vector_b[-1])
    for i in range(size-2, -1, -1):
        y.insert(0, alpha[i]*y[0]+betta[i])

    return y