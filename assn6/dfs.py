"""
Assn5 Problem2
- Inplement the depth first search algorithm from the textbook using Python and the functions in the NetworkX library.
The code must implement all four functions explore, dfs, previsit, and postvisit from the textbook.
The functions must be exactly as they are given in the textbook exceptfor the modifications outlined below.


- The code should work with directed and with undirected graphs.

- Whenever you have a choice between several nodes, always choose the smallesr one
(using Pythons's built-in sorting functions.)
"""

"""
You are only allowed to use library functions/methods for finding the neighbours of a node, 
for getting an iterator over the nodes, and for setting and reading attributes
(if you are implementing option (iii).
In particular, you are not allowed to use the depth first search funcitons from the NetworkX library and any attempt to do so will result in 0 points.
"""

import networkx as nx
"""
- I will use this option: (i) Use global variables(exactly as in the textbook). 
Caution: Do not forget to reset the variables so that dfs can be called multiple times.
"""

clock = 0
pre = {}
post = {}
ccnum = {}
cc = 0

def previsit(v):
    """
    Modify previsit to compute the connected component numbers alongside the pre and post numbers. 
    
    Use the method described in the textbook:
    Chapter 3.2.4
    procedure previsit(v)
    pre[v] = clock
    clock = clock + 1
    """
    global clock, pre, ccnum, cc
    clock += 1
    pre[v] = clock
    ccnum[v] = cc

def postvisit(v):
    """
    Chapter 3.2.4
    procedure postvisit(v)
    post[v] = clock
    clock = clock + 1
    """
    global clock, post
    clock += 1
    post[v] = clock

def explore(G, v):
    """
    Figure 3.3
    procedure explore(G, v)
    Input: G = (V, E) is a graph; v belongs to V
    Output: visited(u) is set to true for all nodes u reachable from v

    visited(v) = true
    previsit(v)
    for each efge (v, u) belongs to E:
        if not visited(u): explore(u)
    postvisit(v)
    """
    previsit(v)
    for u in sorted(G.neighbors(v)):
        if pre[u] == 0:
            explore(G, u)
    postvisit(v)

def dfs(G):
    """
    The function dfs has a NetworkX graph or diagraph 
    as its input and it returns a triple of Python dictionaries(pre, post, ccnum) 
    where the nodes of the graph are the keys and where 
    pre contains the previsit numbers, 
    post contains the post visit numbers, 
    and cc num contains the component numbers.
    """
    """
    Modify dfs to compute the connected component numbers alongside the pre and post numbers. 
    
    Use the method described in the textbook:
    Figure 3.5
    procedure dfs(G)
    for all v belongs to V:
        visited(v) = false
    for all v belongs to V:
        if not visited(v):
            explore(v)
    """
    assert isinstance(G, (nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph))

    global clock, pre, post, ccnum, cc
    clock = 0
    cc = 0
    pre = {v: 0 for v in G.nodes()}
    post = {v: 0 for v in G.nodes()}
    ccnum = {v: 0 for v in G.nodes()}

    for v in sorted(G.nodes()):
        if pre[v] == 0:
            cc += 1
            explore(G, v)

    return dict(pre), dict(post), dict(ccnum)

if __name__ == "__main__":
    """
    At the vary least, your function should produce exactly the same previsit and postvisit numbers for the graph in Figure 3.6 (a) of the textbook as the ones shown in Figure 3.6(b).
    (Of course, professor will be testing them with additional graphs.)
    """
    pass