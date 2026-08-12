import networkx as nx

def generate_graph(n,m):
    # generate a random graph with n vertices and m edges

    G = nx.gnm_random_graph(n,m)
    
    return G

