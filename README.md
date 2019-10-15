# game_of_life_to_stl
My quick little project; translating Conway's Game of Life to 3D model. 

# How it works?
Each new iteration of the field is translated into a layer of 3d cubes, where each live cell represents one cube. 
Next iteration is moved up in z axis for x, where x is the length of a side of the cube.

To run open main.py and a tkinter window will prompt you to select the starting cell positions. After you click run
the simulation will run and when it is finished it will close tkinter window and in the same folder there will be
"test.stl" file, contatining the result.
