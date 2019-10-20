from Celluar import Celluar
import tkinter as tk
import tkinter.filedialog
import numpy as np
class App():
    def __init__(self, n, height, scale):
        """ n represents how big the field is going to be
            scale represents the size of the side of a square in the stl"""
        self.n = n
        self.height = height
        self.scale = scale
        self.square_size = 10
        self.field = np.zeros((self.n+2,self.n+2), dtype=np.bool_)
        self.master = tk.Tk()
        self.canvas = tk.Canvas(master=self.master, 
                                width=self.n*self.square_size, 
                                height=self.n*self.square_size)
        self.canvas.focus_set()
        self.draw_rectangles()
        self.canvas.bind("<Button-1>", self.select)
        self.canvas.bind("<Button-3>", self.deselect)
        self.canvas.pack()

        self.run_button = tk.Button(master=self.master, text="RUN", command=self.run)
        self.run_button.pack()
        self.browse_button = tk.Button(master=self.master, text="SELECT FILE", command=self.read_cells)
        self.browse_button.pack()

        self.master.mainloop()
        
    def draw_rectangles(self):
        for i in range(self.n):
            for j in range(self.n):
                self.canvas.create_rectangle(i*self.square_size, j*self.square_size,
                                            (i+1)*self.square_size, (j+1)*self.square_size, 
                                            fill="yellow" if self.field[i][j] else "red")
    def select(self, event, select=True):
        x = int(event.x/self.square_size)
        y = int(event.y/self.square_size)
        self.field[x][y] = select
        self.canvas.delete("all")
        self.draw_rectangles()

    def deselect(self, event):
        self.select(event, select=False)
        
    def run(self):
        self.celluar = Celluar(self.n, self.scale, self.height, self.field)
        self.celluar.run()
        self.celluar.close()
        self.master.quit()

    def read_cells(self):
        self.filename = tkinter.filedialog.askopenfilename(initialdir=".", title="Select file", 
            filetypes=[("cells files", ".cells")])
        if(len(self.filename) == 0): return
        with open(self.filename, mode="r") as file:
            tmp = list(filter(lambda x: x[0] != "!", file))
            max_x = len(max(tmp))
            max_y = len(tmp)
            file.seek(0)
            i_offset = int(self.n/2 - max_y/2)
            j_offset = int((self.n - max_x)/2)
            j = 0
            for line in file:
                if line[0] != "!":
                    for i in range(len(line)):
                        self.field[i+i_offset][j+j_offset] = line[i] == "O"
                    j+=1
            self.draw_rectangles()
