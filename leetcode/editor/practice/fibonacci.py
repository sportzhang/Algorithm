# -*- coding: utf-8 -*-
"""
斐波那契数列递归实现
"""


def fibonacci(n):
    """
    斐波那契数列：1,1,2,3,5,8,....所以通项公式就是分分f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2)(n>3)
    :param n:斐波那契数列的第n项
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == '__main__':
    result = fibonacci(6)
    print(result)
