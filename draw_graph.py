import matplotlib.pyplot as plt
import networkx as nx
def draw_graph(G, cover):

    pos = nx.spring_layout(G, seed=42)

    colors = []

    for node in G.nodes():
        if node in cover:
            colors.append("red")
        else:
            colors.append("skyblue")
    plt.figure(figsize=(7,7))

    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.title("Minimum Vertex Cover")
    plt.axis("off")
    plt.show()
    plt.close()