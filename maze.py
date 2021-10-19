from graph import Graph
import render
from coveringtree import prim
import random


class Maze:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.graph=self.gen_random()

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
        render.draw_tree(self.graph)

    def gen_maze(self):
        parent=prim(self.graph)
        graph=Graph()
        for u in parent:
            graph.add_arc((u, parent[u]))
            graph.add_arc((parent[u],u))
        return graph

    def gen_random(self):
        rdmgraph= Graph()
        for x in range(self.width):
            for y in range(self.height):
                if x<self.width-1:
                    rdmgraph.add_arc(((x,y),(x+1,y)),random.uniform(0,1))
                    weight1= rdmgraph.arc_weight(((x,y),(x+1,y)))
                    rdmgraph.add_arc(((x+1,y),(x,y)),weight1)
                if y<self.height-1:
                    rdmgraph.add_arc(((x,y),(x, y+1)),random.uniform(0,1))
                    weight2= rdmgraph.arc_weight(((x,y),(x, y+1)))
                    rdmgraph.add_arc(((x,y+1),(x,y)),weight2)
        return rdmgraph



