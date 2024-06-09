import networkx as nx
from algorithmx import jupyter_canvas

canvas = jupyter_canvas()

canvas.nodes(G.nodes).add()
canvas.edges(G.edges).add()

canvas  