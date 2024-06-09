from networkx import *
import networkx as nx
import matplotlib.pyplot as plt

def create(v1_v2_e, kol_v):
    G = nx.MultiGraph()
    for i in range(kol_v):
        G.add_node(i)
    for i in range(len(v1_v2_e)):
        G.add_edge(v1_v2_e[i][0], v1_v2_e[i][1], weight=v1_v2_e[i][2])
    
    draw(G)
    