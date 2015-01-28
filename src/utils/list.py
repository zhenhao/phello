__author__ = 'wangzhenhao'


class List:
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()

    def dump(self):
        print(self.l)

    def empty(self):
        return len(self.l) == 0