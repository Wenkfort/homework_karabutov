# f(x) = x^3 + 6x^2 - 10x + 6
# f'(x) = 3x^2 + 12x - 10
# f'(x) = 0 => x1 ~ -4.7 , x2 = 0.7 

import numpy as np

def function(x):
    return x**3 + 6*(x**2) - 10 * x + 6

# метод равномерного поиска
def first_method(a, b, N):
    xi = np.arange(a, b, (b - a) / N)
    res = [function(x) for x in xi]
    idx = np.where(res == np.min(res))
    return xi[idx[0][0]], res[idx[0][0]]

def second_method(a, b, l):
    length = 
    x_k = (a, b) / 2
    res = function(x_k)
    y_k = a + / 4
    return 0

def main():
    x, y = first_method(-5, 2, 2000)
    print (x, y)
    result = second_method(-5, 2, 0.001)

if __name__ == '__main__':
    main()