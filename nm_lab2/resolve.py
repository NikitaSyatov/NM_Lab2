#!/usr/bin/env python3

import math
from scipy import integrate
from threediag_matrix_alg import Progonka

# In[0]: константы для истинного решения тестовой задачи
CONST = [[-4.55134, 3.44568], [0.943942, 5.0601]]

# In[1]: константы для начального и конечного узла, точка разрыва кси
KSI = 0.4
MU1 = 0
MU2 = 1

# In[2]: функции для решения тестовой задачи
def test_k1(x):
    return 1/1.4

def test_k2(x):
    return 1/0.4

def test_q1(x):
    return 0.4

def test_q2(x):
    return 0.16

def test_f1(x):
    return 0.4

def test_f2(x):
    return math.exp(-0.4)

# In[3]: функции для решения основной задачи
def k1(x):
    return 1/(x+1)

def k2(x):
    return 1/x

def q1(x):
    return x

def q2(x):
    return x*x

def f1(x):
    return x

def f2(x):
    return math.exp(-x)

# In[4]: истинное решение тестовой задачи
def u1(x):
    return CONST[0][0] * math.exp(x * math.sqrt(2/7)) + CONST[0][1] * math.exp(-x * math.sqrt(2/7)) + 1
 
def u2(x):
    return CONST[1][0] * math.exp(x * math.sqrt(2/5)) + CONST[1][1] * math.exp(-x * math.sqrt(2/5)) + math.exp(-0.4)/0.16

# расчет коэфициентов в уравнении selector = 1 - тестовая
def calc_ai(x, step, selector):
    xi = x
    xi_1 = x - step
    
    if selector:
        k1 = test_k1
        k2 = test_k2

    if KSI >= xi:
        return 1/((1/step)*integrate.quad(k1, xi_1, xi)[0])
    elif KSI < xi and KSI > xi_1:
        return 1/((1/step)*(integrate.quad(k1, xi_1, KSI)[0] + integrate.quad(k2, KSI, xi)[0]))
    else:
        return 1/((1/step)*integrate.quad(k2, xi_1, xi)[0])
    
def calc_di(x, step, selector):
    xi_up = x + step/2
    xi_down = x - step/2
    
    if selector:
        q1 = test_q1
        q2 = test_q2
    
    if KSI >= xi_up:
        return ((1/step)*integrate.quad(q1, xi_down, xi_up)[0])
    elif KSI < xi_up and KSI > xi_down:
        return ((1/step)*(integrate.quad(q1, xi_down, KSI)[0] + integrate.quad(q2, KSI, xi_up)[0]))
    else:
        return ((1/step)*integrate.quad(q2, xi_down, xi_up)[0])
    
def calc_phi_i(x, step, selector):
    xi_up = x + step/2
    xi_down = x - step/2
    
    if selector:
        f1 = test_f1
        f2 = test_f2

    if KSI >= xi_up:
        return ((1/step)*integrate.quad(f1, xi_down, xi_up)[0])
    elif KSI < xi_up and KSI > xi_down:
        return ((1/step)*(integrate.quad(f1, xi_down, KSI)[0] + integrate.quad(f2, KSI, xi_up)[0]))
    else:
        return ((1/step)*integrate.quad(f2, xi_down, xi_up)[0])
    
# построение 3 диагональной матрицы
def method_balance(n, sel):
    matrix_A = []
    vector_b = []
    
    step = 1/n
    n += 1
    matrix_A.append([0, MU1, 0])
    vector_b.append(-calc_phi_i(0, step, sel))

    for i in range(1, n-1):
        xi = i*step
        matrix_A.append([calc_ai(xi, step, sel)/(step*step),
                          -calc_ai(xi, step, sel)/(step*step)+calc_ai(xi+step, step, sel)/(step*step)-calc_di(xi, step, sel),
                           calc_ai(xi+step, step, sel)/(step*step)])
        vector_b.append(-calc_phi_i(xi, step, sel))

    matrix_A.append([0, MU2, 0])
    vector_b.append(-calc_phi_i(1, step, sel))

    print(matrix_A)
    print(vector_b)

    v = Progonka(matrix_A, vector_b, len(vector_b))
    x = [i*step for i in range(n)]
    u = [u1(xi) for xi in x]

    print(v)
    print(x)
    print(u)

if __name__ == '__main__':
    method_balance(5, 1)



        