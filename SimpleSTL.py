import struct
import numpy as np

class SimpleSTL():
    def __init__(self, scale=0):
        self.scale = scale
        self.n_facets = 0
        self.file = open("test.stl", mode="wb")
        self.file.write(bytes(80))
        self.file.write(struct.pack("<I", 0))

    def draw_facet(self, p1, p2, p3):
        self.n_facets += 1
        n = np.cross([a-b for a,b in zip(p1,p2)], [a-b for a,b in zip(p1, p3)])
        for i in [n,p1,p2,p3]:
            self.file.write(struct.pack("<fff", *i))
        self.file.write(bytes(2))

    def draw_square(self, p1, p2, p3, p4):
        self.draw_facet(p1, p2, p3)
        self.draw_facet(p4, p3, p2)

    def draw_cube(self, x, y, z):
        s = self.scale
        self.draw_square([x,y,z],[x,y+s,z],[x,y,z+s],[x,y+s,z+s])
        self.draw_square([x,y,z],[x,y+s,z],[x+s,y,z],[x+s,y+s,z])
        self.draw_square([x,y,z],[x+s,y,z],[x,y,z+s],[x+s,y,z+s])
        self.draw_square([x+s,y,z],[x+s,y+s,z],[x+s,y,z+s],[x+s,y+s,z+s])
        self.draw_square([x,y,z+s],[x,y+s,z+s],[x+s,y,z+s],[x+s,y+s,z+s])    
        self.draw_square([x,y+s,z],[x+s,y+s,z],[x,y+s,z+s],[x+s,y+s,z+s])

    def close(self):
        self.file.seek(80)
        self.file.write(struct.pack("<I", self.n_facets))
        self.file.close()