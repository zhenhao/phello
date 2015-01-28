__author__ = 'wangzhenhao'

from utils.list import List

if __name__ == '__main__':
    l = List()
    for i in range(0, 10):
        l.push(i)

    while not l.empty():
        print(l.pop())