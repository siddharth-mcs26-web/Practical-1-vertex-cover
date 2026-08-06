import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16, font_weight='bold')
plt.title("Graph Representation", fontsize=20)
plt.show() 