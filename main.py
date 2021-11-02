from maze import Maze
from hexagonalmaze import HexagonalMaze


maze1=HexagonalMaze(10,10)

maze1.generate_maze()
maze1.draw_hex_maze_with_path()

maze2=Maze(40,40)
maze2.generate_maze()
maze2.draw_square_maze_with_path()