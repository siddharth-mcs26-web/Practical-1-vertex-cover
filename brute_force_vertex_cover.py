def brute_force_vertex_cover(G):
    n = G.number_of_nodes()
    edges = list(G.edges())
    number_of_subsets = 1 << n
    size_of_vertex_cover = n+1
    vertex_cover = []

    for mask in range(number_of_subsets):

        cover = mask_to_vertex_cover(mask, n)

        if is_vertex_cover(edges, cover):
            if len(cover) < size_of_vertex_cover:
                size_of_vertex_cover = len(cover)
                vertex_cover = cover
                
    return vertex_cover
        
    