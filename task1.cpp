#define CONST1_1 -16.56308888689557748823
#define CONST1_2 -6.39152872148917623891
#define CONST2_1 18.98195831762380717592
#define CONST2_2 -70.99761651465712118978

#define KSI 0.4
#define MU1 0
#define MU2 1

#define TEST_K1 1.4
#define TEST_K2 0.4
#define TEST_Q1 0.4
#define TEST_Q2 0.16
#define TEST_F1 0.4
#define TEST_F2 std::exp(-0.4)

#include <iostream>
#include <cmath>
#include <vector>

double k1(double x)
{
    return x+1;
}

double k2(double x)
{
    return x;
}

double q1(double x)
{
    return x;
}

double q2(double x)
{
    return x*x;
}

double f1(double x)
{
    return x;
}

double f2(double x)
{
    return std::exp(-x);
}

double u1(double x)
{
    return CONST1_1 * std::exp(x * std::sqrt(2/7)) + CONST1_2 * std::exp(-x * std::sqrt(2/7)) + 1;
}

double u2(double x)
{
    return CONST2_1 * std::exp(x * std::sqrt(2/5)) + CONST2_2 * std::exp(-x * std::sqrt(2/5)) + std::exp(-0.4)/0.16;
}

void method_balance(int n, int choose = 1) //choose = 1 - test, choose = 0 - main problem
{
    std::vector<std::vector<double>> matrix_with_3_diagonal(n, std::vector<double>(3, 0));

    std::vector<double> b(n);
// инициализация 3 диагональной матрицы
    // for (int i = 0; i < n; i++)
    // {
    //     matrix_with_3_diagonal[i][0] = koef1; // коэф при v_i-1
    //     matrix_with_3_diagonal[i][1] = koef2; // коэф при v_i
    //     matrix_with_3_diagonal[i][2] = koef3; // коэф при v_i+1
    // }

// прогонка

// вывод матрицы
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < 3; j++)
    //         std::cout << matrix_with_3_diagonal[i][j] << "\t";
    //     std::cout << "\n";
    // }
}

int main()
{
    method_balance(3);

    return 0;
}

