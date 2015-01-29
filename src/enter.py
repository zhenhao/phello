__author__ = 'wangzhenhao'

from utils.container import *
from random import randint

if __name__ == '__main__':
    t = btree.BTree()

    for i in range(0, 10):
        t.insert(randint(0, 100))

    t.show()