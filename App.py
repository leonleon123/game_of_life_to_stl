from Celluar import Celluar
import tkinter as tk
import numpy as np

class App():
    def __init__(self, n, scale):
        """ n represents how big the field is going to be
            scale represents the size of the side of a square in the stl"""
        self.n = n
        self.size = 20
        self.scale = scale
        self.field = np.zeros((self.n+2,self.n+2), dtype=np.bool_)
        self.master = tk.Tk()
        self.canvas = tk.Canvas(master=self.master, 
                                width=self.n*self.size, 
                                height=self.n*self.size)
        self.draw_rectangles()
        self.canvas.bind("<Button-1>", self.select)
        self.canvas.bind("<Button-3>", self.deselect)
        self.run_button = tk.Button(master=self.master, text="RUN", command=self.run)
        self.canvas.pack()
        self.run_button.pack()
        self.master.mainloop()
        
        
    def draw_rectangles(self):
        for i in range(self.n):
            for j in range(self.n):
                self.canvas.create_rectangle(i*self.size, j*self.size,
                                            (i+1)*self.size, (j+1)*self.size, 
                                            fill="yellow" if self.field[i][j] else "red")
    def select(self, event, select=True):
        x = int(event.x/self.size)
        y = int(event.y/self.size)
        self.field[x][y] = select
        self.canvas.delete("all")
        self.draw_rectangles()

    def deselect(self, event):
        self.select(event, select=False)
        
    def run(self):
        self.celluar = Celluar(self.n, self.scale, self.field)
        self.celluar.run()
        self.celluar.close()
        self.master.quit()