#!/usr/bin/env python3

import math
from scipy import integrate
from new_progon import Progonka

# In[0]: константы для истинного решения тестовой задачи
CONST = [[0.7348403689121157, -1.7348403689121157], [-0.6706091081659652, -3.6275438934922134]]

# In[1]: константы для начального и конечного узла, точка разрыва кси
KSI = 0.4
MU1 = 0
MU2 = 1

# In[2]: функции для решения тестовой задачи
def test_k1(x):
    return 5.0/7.0

def test_k2(x):
    return 5.0/2.0

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
def u(x):
    if x < KSI:
        return CONST[0][0] * math.exp(x * math.sqrt(2./7.)) + CONST[0][1] * math.exp(-x * math.sqrt(2./7.)) + 1.
    else:
        return CONST[1][0] * math.exp(x * math.sqrt(0.4)) + CONST[1][1] * (math.exp(-x * math.sqrt(0.4))) + math.exp(-0.4)/0.16

# расчет коэфициентов в уравнении selector = 1 - тестовая
def calc_ai(x, step, selector):
    xi = x
    xi_1 = x - step
    
    if selector == 1:
        this_k1 = test_k1
        this_k2 = test_k2
    else:
        this_k1 = k1
        this_k2 = k2

    # if KSI >= xi:
    #     return step/(integrate.quad(this_k1, xi_1, xi)[0])
    # elif KSI < xi and KSI > xi_1:
    #     return step/(integrate.quad(this_k1, xi_1, KSI)[0] + integrate.quad(this_k2, KSI, xi)[0])
    # else:
    #     return step/(integrate.quad(this_k2, xi_1, xi)[0])
    if KSI >= xi:
        return this_k1(xi - step/2.0)
    elif KSI <= xi_1:
        return this_k2(xi - step/2.0)
    else:
        return ((1/step)*( ((KSI - xi_1) / (this_k1((xi_1 + KSI)/2.0))) + ((xi - KSI) / (this_k2((KSI + xi)/2.0))) ))**(-1)
    
def calc_di(x, step, selector):
    xi_up = x + step/2.0
    xi_down = x - step/2.0
    
    if selector == 1:
        this_q1 = test_q1
        this_q2 = test_q2
    else:
        this_q1 = q1
        this_q2 = q2
    
    # if KSI >= xi_up:
    #     return ((1/step)*integrate.quad(this_q1, xi_down, xi_up)[0])
    # elif KSI < xi_up and KSI > xi_down:
    #     return ((1/step)*(integrate.quad(this_q1, xi_down, KSI)[0] + integrate.quad(this_q2, KSI, xi_up)[0]))
    # else:
    #     return ((1/step)*integrate.quad(this_q2, xi_down, xi_up)[0])
    if KSI >= xi_up:
        return this_q1(x)
    elif KSI <= xi_down:
        return this_q2(x)
    else:
        return (1/step)*((this_q1((xi_down + KSI)/2.0) * (KSI - xi_down)) + (this_q2((KSI + xi_up)/2.0) * (xi_up - KSI)))
    
def calc_phi_i(x, step, selector):
    xi_up = x + step/2.0
    xi_down = x - step/2.0
    
    if selector == 1:
        this_f1 = test_f1
        this_f2 = test_f2
    else:
        this_f1 = f1
        this_f2 = f2

    # if KSI > xi_up:
    #     return (1/step)*(integrate.quad(this_f1, xi_down, xi_up)[0])
    # elif KSI < xi_up and KSI > xi_down:
    #     return ((1/step)*(integrate.quad(this_f1, xi_down, KSI)[0] + integrate.quad(this_f2, KSI, xi_up)[0]))
    # else:
    #     return ((1/step)*integrate.quad(this_f2, xi_down, xi_up)[0])
    if KSI >= xi_up:
        return this_f1(x)
    elif KSI <= xi_down:
        return this_f2(x)
    else:
        return (1/step)*(this_f1((xi_down + KSI)/2.0) * (KSI - xi_down) + this_f2((KSI + xi_up)/2.0) * (xi_up - KSI) )
    
# построение 3 диагональной матрицы
def method_balance(n, sel):
    matrix_A = []
    vector_b = []
    
    step = 1/n
    n += 1
    xi = 0

    matrix_A.append([1, 0, 0])
    vector_b.append(MU1)
    
    for i in range(1, n-1):
        xi = i*step
        print(calc_di(xi, step, sel))
        matrix_A.append([calc_ai(xi, step, sel)/(step*step),
                          -(calc_ai(xi, step, sel)+calc_ai(xi+step, step, sel))/(step*step)-1,
                           calc_ai(xi+step, step, sel)/(step*step)])
        vector_b.append(-calc_phi_i(xi, step, sel))

    matrix_A.append([0, 0, 1])
    vector_b.append(MU2)

    for i in range(len(matrix_A)):
        print(str(matrix_A[i]))
    print('\n')
    print(vector_b)

    v = Progonka(matrix_A, vector_b)
    x = [i*step for i in range(n)]
    vec_u = [u(i) for i in x]

    print('\n')
    print(v)
    print(x)
    print(vec_u)

    return x, v

if __name__ == '__main__':
    method_balance(2, 1)
   