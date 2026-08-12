def is_vertex_cover(edges, cover):
    for u,v in edges:
        for i in cover:
            if u == i or v == i:
                break
        else:
            return False
    return True