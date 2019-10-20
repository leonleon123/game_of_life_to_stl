from App import App
import sys
app_help = """Usage: python main.py <n> <height>\nwhere:
    -n          size of a side of the simulation field, which is a square, so n^2 squares
    -height     number of generations, number of layers in finished 3d model"""

if __name__=="__main__":
    if sys.argv[1] == "-help" or sys.argv[1] == "/?":
        print(app_help)
        quit()
    app = App(int(sys.argv[1]), int(sys.argv[2]), 5.0)
