import networkx as nx
import random
def generate_graph(n,m):
    # generate a random graph with n vertices and m edges

    edges = []
    while(len(edges) < m):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        if a != b:
            if (a,b) in edges or (b,a) in edges:
                continue
            else:
                edges.append((a,b))
    
    f = open(f"graph{m}.txt", 'a')
    for i in edges:
        s = str(i) + '\n'
        f.write(s)
generate_graph(10,34)    