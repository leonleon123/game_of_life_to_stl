import numpy as np
from SimpleSTL import SimpleSTL

class Celluar():
    def __init__(self, n, size, field):
        self.n = n
        self.size = size
        self.level = 0
        self.z = 0.0
        self.field = field
        self.STL_writer = SimpleSTL(size=self.size)

    def print_field(self):
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                print("O" if self.field[i][j] else ".", end="")
            print()

    def check(self, x, y):
        cells = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i != x or j != y:
                    cells+= 1 if self.field[i][j] else 0
        return (cells == 2 if self.field[x][y] else False) or cells == 3

    def update(self):
        temp = np.zeros((self.n+2,self.n+2), dtype=np.bool_)
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                temp[i][j] = self.check(i,j)
        return temp

    def run(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.field[i][j]:
                    self.STL_writer.draw_cube(i*self.size, j*self.size, self.z)
        self.z += self.size
        self.level += 1
        self.field = self.update()
        if(self.level < self.n * 2):
            self.run()

    def close(self):
        self.STL_writer.close()