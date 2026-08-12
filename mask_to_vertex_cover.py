def mask_to_vertex_cover(mask, n):
    vertex_cover = []
    for i in range(n):
        if (mask >> i)& 1:
            vertex_cover.append(i)

    return vertex_cover
    