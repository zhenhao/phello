__author__ = 'wangzhenhao'


class List:
    def __init__(self):
        self.l = []

    def append(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()

    def __str__(self):
        return str(self.l)

    def empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

    def __bool__(self):
        return not self.empty()