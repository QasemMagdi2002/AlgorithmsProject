import sys
def prim(graph):
    num_vertices = len(graph)
    selected_vertices = [0]
    remaining_vertices = list(range(1, num_vertices))

    while remaining_vertices:
        min_edge = sys.maxsize
        for u in selected_vertices:
            for v in remaining_vertices:
                if graph[u][v] < min_edge:
                    min_edge = graph[u][v]
                    min_edge_vertices = (u, v)

        selected_vertices.append(min_edge_vertices[1])
        remaining_vertices.remove(min_edge_vertices[1])
        print(f"Edge added: {min_edge_vertices} with weight {min_edge}")

# Example usage:
graph = [
    [0, 2, 0, 4, 0, 5, 0],  # a
    [2, 0, 7, 1, 3, 8, 4],  # b
    [0, 7, 0, 0, 10, 0, 6], # c
    [4, 1, 0, 0, 2, 0, 0],  # d
    [0, 3, 10, 2, 0, 0, 0], # e
    [5, 8, 0, 0, 0, 0, 1],  # f
    [0, 4, 6, 0, 0, 1, 0]   # g
]
prim(graph)