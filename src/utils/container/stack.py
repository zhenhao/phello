__author__ = 'wangzhenhao'


class Stack:
    def __init__(self):
        self.l = []

    def __str__(self):
        return str(self.l)

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()

    def empty(self):
        return 0 == len(self.l)

    def __bool__(self):
        return not self.empty();

    def __len__(self):
        return len(self.l)
