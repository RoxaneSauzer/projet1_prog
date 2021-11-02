import math
from graph import Graph

def get_min_cost(cost, choices):
    mincost=math.inf
    min=0
    for u in choices:
        if cost[u]<=mincost:
            mincost=cost[u]
            min=u
    return min


def prim(graph):
    cost={}
    parent={}

    for v in graph.nodes():
        cost[v]=math.inf

    choices=graph.nodes()
    while len(choices)!=0:
        min= get_min_cost(cost,choices)
        choices.remove(min)

        for v in graph.successors(min):
            if v in choices and graph.arc_weight((min,v))<cost[v]:
                cost[v]= graph.arc_weight((min,v))
                parent[v]=min

    return parent