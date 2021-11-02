
from graph import Graph
from maze import Maze
import random

class HexagonalMaze(Maze):
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.graph=self.generate_graph()


    def generate_graph(self):
        graph= Graph()
        for x in range(self.width):
            for y in range(self.height):
                if x<self.width-1:
                    graph.add_arc(((x,y),(x+1,y)),random.uniform(0,1))
                    weight1 = graph.arc_weight(((x,y),(x+1,y)))
                    graph.add_arc(((x+1,y),(x,y)), weight1)
                if y<self.height-1:
                    if y%2==0:
                        graph.add_arc(((x,y),(x, y+1)),random.uniform(0,1))
                        weight2 = graph.arc_weight(((x,y),(x,y+1)))
                        graph.add_arc(((x,y+1),(x,y)),weight2)
                        if x>0:
                            graph.add_arc(((x,y),(x-1,y+1)), random.uniform(0,1))
                            weight3 = graph.arc_weight(((x,y),(x-1,y+1)))
                            graph.add_arc(((x-1,y+1),(x,y)), weight3)
                    else:
                        graph.add_arc(((x,y),(x,y+1)),random.uniform(0,1))
                        weight4 = graph.arc_weight(((x,y),(x,y+1)))
                        graph.add_arc(((x,y+1),(x,y)),weight4)
                        if x<self.width-1:
                            graph.add_arc(((x,y),(x+1,y+1)),random.uniform(0,1))
                            weight5 = graph.arc_weight(((x,y),(x+1,y+1)))
                            graph.add_arc(((x+1,y+1),(x,y)), weight5)

        return graph