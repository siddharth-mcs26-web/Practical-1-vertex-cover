from graph_generator import generate_graph
from brute_force_vertex_cover import brute_force_vertex_cover
from read_output import read_file
from draw_graph import draw_graph
import time
n = 10
results = []
for m in range(15, 46, 5):
    generate_graph(n,m)
    graph = read_file(f"graph{m}.txt")
    start = time.perf_counter()
    cover = brute_force_vertex_cover(graph)
    print(cover)
    end = time.perf_counter()
    results.append({
        "n" : n,
        "m" : m,
        "vc_size" : len(cover),
        "time" : end-start
    })
    draw_graph(graph, cover)
for r in results:
    print(
        f"({r['n']},{r['m']})\t\t"
        f"{r['vc_size']}\t"
        f"{r['time']:.6f} s"
    )
