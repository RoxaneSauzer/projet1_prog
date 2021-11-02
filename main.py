import render
from maze import Maze
import graph
import coveringtree
from hexagonalmaze import HexagonalMaze


maze=HexagonalMaze(10,20)

maze.generate_maze()
render.draw_hex_maze(maze.graph, maze.get_solution())