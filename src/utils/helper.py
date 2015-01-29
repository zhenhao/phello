__author__ = 'wangzhenhao'


def hanoi(a='A', b='B', c='C', n=1):
    if n < 1:
        pass
    elif n == 1:
        print(a + ' -> ' + c)
    else:
        hanoi(a, c, b, n - 1)
        print(a + ' -> ' + c)
        hanoi(b, a, c, n - 1)