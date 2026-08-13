from graph_generator import generate_graph
from brute_force_vertex_cover import brute_force_vertex_cover
from draw_graph import draw_graph
n = 10
for m in range(15, 46, 5):
    G = generate_graph(n,m)
    cover = brute_force_vertex_cover(G)
    print(cover)
    draw_graph(G, cover)
