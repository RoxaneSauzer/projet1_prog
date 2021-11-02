from graph import Graph
import render
from coveringtree import prim
import random


class Maze:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.graph=self.generate_random()


    def generate_graph(self):
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

    def draw_hex(self):
        render.draw_hex_maze(self.graph, draw_coordinates=True)

    def draw_hex_maze_with_path(self):
        render.draw_hex_maze(self.graph, self.get_solution())

    def draw_square(self):
        render.draw_square_maze(self.graph,draw_coordinates=True)

    def draw_square_maze_with_path(self):
        render.draw_square_maze(self.graph, self.get_solution())


    def generate_maze(self):
        parent=prim(self.graph)
        graph=Graph()
        for u in parent:
            graph.add_arc((u, parent[u]))
            graph.add_arc((parent[u],u))
        self.graph = graph

    def generate_random(self):
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


    def explore(self, current, path, seen, end):
        graph=self.graph

        seen.append(current)
        path.append(current)
        if current == end:
            return True
        for neighbor in graph.successors(current):
            if neighbor not in seen:
                if self.explore(neighbor,path,seen,end):
                    return True
        else:
            path.remove(current)
            return False

    def get_solution(self):
        path=[]
        self.explore((0,0), path, [], (self.width - 1, self.height -1))
        return path

    def generate_vertically_biased_grid(self, weight=random.uniform(0,1)):
        graph= Graph()
        for x in range(self.width):
            for y in range(self.height):
                if x<self.width-1:
                    graph.add_arc(((x,y),(x+1,y)),random.uniform(0,1))
                    weight1= graph.arc_weight(((x,y),(x+1,y)))
                    graph.add_arc(((x+1,y),(x,y)),weight1)
                if y<self.height-1:
                    graph.add_arc(((x,y),(x, y+1)),random.uniform(0,1)+weight)
                    weight2= graph.arc_weight(((x,y),(x, y+1)))
                    graph.add_arc(((x,y+1),(x,y)),weight2)
        return graph

    def generate_horizontally_biased_grid(self, weight=random.uniform(0,1)):
        graph= Graph()
        for x in range(self.width):
            for y in range(self.height):
                if x<self.width-1:
                    graph.add_arc(((x,y),(x+1,y)),random.uniform(0,1)+weight)
                    weight1= graph.arc_weight(((x,y),(x+1,y)))
                    graph.add_arc(((x+1,y),(x,y)),weight1)
                if y<self.height-1:
                    graph.add_arc(((x,y),(x, y+1)),random.uniform(0,1))
                    weight2= graph.arc_weight(((x,y),(x, y+1)))
                    graph.add_arc(((x,y+1),(x,y)),weight2)
        return graph

