# f(x) = x^3 + 6x^2 - 10x + 6
# f'(x) = 3x^2 + 12x - 10
# f'(x) = 0 => x1 ~ -4.7 , x2 = 0.7 

import numpy as np

# возвращает значении функции в точке x
def function(x):
    #return 2*x**2 - 12*x
    return x**3 + 6*(x**2) - 10 * x + 6

def function_first_derivative(x):
    return 3*x**2 + 12*x - 10

# метод равномерного поиска
def first_method(a, b, N):
    if a > b or N < 1:
        return
    xi = np.arange(a, b, (b - a) / N)
    res = [function(x) for x in xi]
    idx = np.where(res == np.min(res))
    return xi[idx[0][0]], res[idx[0][0]]

# метод деления отрезка пополам
def second_method(a, b, l):
    if a > b or l <= 0 or l >= (b - a):
        return
    middle_point = (a + b) / 2
    length = b - a
    while length > l:
        x_ck = (a + b) / 2
        y_k = a + length / 4
        z_k = b - length / 4

        f_x_ck = function(x_ck)
        f_y_k = function(y_k)
        f_z_k = function(z_k)

        if f_y_k < f_x_ck:
            b = x_ck
            middle_point = y_k
        elif f_y_k >= f_x_ck: 
            if f_z_k < f_x_ck:
                a = x_ck
                middle_point = z_k
            if f_z_k >= f_x_ck:
                a = y_k
                b = z_k
                middle_point = x_ck
        length = b - a
    return middle_point, function(middle_point)

# метод золотого сечения
def third_method(a, b, l):
    if a > b or l <= 0 or l >= (b - a):
        return

    length = b - a
    y = a + (b - a) * (3 - np.sqrt(5)) / 2
    z = a + b - y

    while length > l:
        f_y = function(y)
        f_z = function(z)
        if f_y <= f_z:
            b = z
            z = y
            y = a + b - y
        else:
            a = y
            y = z
            z = a + b - z
        length = b - a

    x_answer = (a + b) / 2
    return x_answer, function(x_answer)

# метод Фибоначчи
def fourth_method(a, b, l, e):
    if a > b or l <= 0 or e <= 0 or l >= (b - a):
        return

    length = b - a
    fibonachi_numbers = find_fibonachi(length, l)
    N = len(fibonachi_numbers) - 1

    k = 0
    y = a + (b - a) * fibonachi_numbers[N - 2] / fibonachi_numbers[N]
    z = a + (b - a) * fibonachi_numbers[N - 1] / fibonachi_numbers[N]
    
    while length > l:
        f_y = function(y)
        f_z = function(z)
        if f_y <= f_z:
            b = z
            z = y
            y = a + (b - a) * fibonachi_numbers[N - k - 3] / fibonachi_numbers[N - k - 1]
        else:
            a = y
            y = z
            z = a + (b - a) * fibonachi_numbers[N - k - 2] / fibonachi_numbers[N - k - 1]  
        
        # last calculating
        if k == N - 3:
            f_y = function(y)
            z = y + e
            f_z = function(z)
            if f_y <= f_z:
                b = z
                z = y
                y = a + (b - a) * fibonachi_numbers[N - k - 3] / fibonachi_numbers[N - k - 1]
            else:
                a = y
                y = z
                z = a + (b - a) * fibonachi_numbers[N - k - 2] / fibonachi_numbers[N - k - 1]  
        length = b - a  
        k += 1
    x_answer = (a + b) / 2
    return x_answer, function(x_answer)

def find_fibonachi(length, l):
    # 1, 1, 2, 3, 5, 8, 13, ... 
    fibonachi_numbers = []

    number = number_= 1
    fibonachi_numbers.append(number)
    fibonachi_numbers.append(number_)
    while number < length / l:
        temp = number
        number += number_
        number_ = temp
        fibonachi_numbers.append(number)
    return fibonachi_numbers


# метод градиентного спуска с постоянным шагом
def gradient(x0, t_k, e, e1, e2, M):
    # градиент функции в точке x0
    x_ = x0
    k = 0
    grad_f = function_first_derivative(x_)
    while abs(grad_f) > e1 and k < M:
        x = x_ - t_k * grad_f
        f_x = function(x)
        f_x_ = function(x_)
        if f_x - f_x_ < 0:
            if abs(x - x_) < e2 and abs(f_x - f_x_) < e2:
                return x, function(x)
            else:
                grad_f = function_first_derivative(x)
                x_ = x
        else:
            t_k = t_k / 2
        k += 1
    return x, function(x)

def main():
    print ('result of first method:')
    x, y = first_method(-5, 2, 2000)
    print ('x = ',x,', y = ',y)
    
    print ('result of second method:')
    x, y = second_method(-5, 2, 0.001)
    print ('x = ',x,', y = ',y)

    print ('result of third method:')
    x, y = third_method(-5, 2, 0.001)
    print ('x = ',x,', y = ',y)    

    print ('result of fourth method:')
    x, y = fourth_method(-5, 2, 0.001, 0.0001)
    print ('x = ',x,', y = ',y)   

    print ('method of grdient downgrade')
    x, y = gradient(0, 0.0001, 0.0001, 0.0001, 0.0001, 10000)
    print ('x = ',x,', y = ',y)   

if __name__ == '__main__':
    main()