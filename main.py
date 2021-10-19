import render
from maze import Maze
import graph
import coveringtree


maze=Maze(10,10)
render.draw_tree(maze.gen_maze())