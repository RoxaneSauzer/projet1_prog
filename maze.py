from graph import Graph
import render
from coveringtree import prim


class Maze:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def gen_graph(self):
        graph= Graph()
        for x in range(self.width):
            for y in range(self.height):
                if x<self.width-1:
                    graph.add_arc(((x,y),(x+1,y)))
                    graph.add_arc(((x+1,y),(x,y)))
                if y<self.height-1:
                    graph.add_arc(((x,y),(x, y+1)))
                    graph.add_arc(((x,y+1),(x,y)))
        return graph

    def draw(self):
        render.draw_tree(self.gen_graph())

    def gen_maze(self):
        parent=prim(self.gen_graph())
        graph=Graph()





m=Maze(2,2)

print(prim(m.gen_graph()))