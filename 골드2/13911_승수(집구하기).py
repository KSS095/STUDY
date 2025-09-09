def f_w():
    pass


V, E = map(int, input().split())    # 정점의 개수, 도로의 개수
edges = [[0] * V for _ in range(V)]

for i in range(E):
    u, v, w = map(int, input().split())
    edges[u - 1][v - 1] = w

