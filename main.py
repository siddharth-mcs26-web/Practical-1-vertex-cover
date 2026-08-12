n = 10
for m in range(15, 46, 5):
    G = generate_graph(n,m)
    cover = brute_force_vertex_cover(G)
    print(cover)
    draw_graph(G, cover)
