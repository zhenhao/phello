__author__ = 'wangzhenhao'


class Queen:
    def __init__(self, n=8):
        self.N = n
        self.t = 0
        self.Q = []
        for i in range(0, self.N):
            self.Q.append(i)

    def attack(self, n):
        for i in range(0, n):
            if self.Q[n] == self.Q[i] or n + self.Q[n] == i + self.Q[i] or n - self.Q[n] == i - self.Q[i]:
                return True
        return False

    def answer(self):
        self.put(0)

    def put(self, n):
        if n == self.N:
            self.draw()
        else:
            for i in range(0, self.N):
                self.Q[n] = i
                if not self.attack(n):
                    self.put(n + 1)

    def draw(self):
        self.t += 1
        print('==========', self.t, '==========')
        for i in self.Q:
            for j in range(0, self.N):
                if i == j:
                    print('Q', end='')
                else:
                    print('-', end='')
            print()
