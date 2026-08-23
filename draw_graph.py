import matplotlib.pyplot as plt
import networkx as nx
def draw_graph(edges, cover):
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(range(10))
    colors = []
    for node in G.nodes():
        if node in cover:
            colors.append('red')
        else:
            colors.append('lightblue')
    nx.draw(G,node_color=colors, with_labels=True)
    plt.show()

draw_graph([(7, 6), (6, 3), (4, 7), (6, 2), (6, 9), (5, 0), (7, 8), (4, 5), (0, 8), (6, 5), (7, 9), (4, 9), (2, 3), (3, 1), (2, 4), (2, 8), (9, 8), (9, 0), (0, 4), (8, 5), (2, 9), (1, 0), (1, 6), (4, 6), (9, 3), (6, 8), (3, 8), (2, 7), (5, 3), (2, 0), (5, 1), (7, 3), (1, 2), (1, 9)], [5,6])
    