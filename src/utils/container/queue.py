__author__ = 'wangzhenhao'


class Queue:
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.insert(0, x)

    def pop(self):
        return self.l.pop()

    def empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

    def __bool__(self):
        return not self.empty()
