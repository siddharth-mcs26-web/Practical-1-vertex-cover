from graph_generator import generate_graph
from brute_force_vertex_cover import brute_force_vertex_cover
from read_output import read_file
from draw_graph import draw_graph
n = 10
for m in range(15, 46, 5):
    generate_graph(n,m)
    graph = read_file(f"graph{m}.txt")
    cover = brute_force_vertex_cover(graph)
    draw_graph(graph, cover)
