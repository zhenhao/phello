#!/usr/bin/env python

from random import randint
from utils.container import *

__author__ = 'wangzhenhao'


if __name__ == '__main__':
    t = btree.BTree()

    for i in range(0, 10):
        t.insert(randint(0, 100))

    t.show()
