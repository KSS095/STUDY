from collections import deque

#     상  하 좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(start_r, start_c):
    if (start_r, start_c) == (row - 1, col - 1): return 1

    queue = deque()
    queue.append((start_r, start_c))

    dist = [[-1 for _ in range(col)] for _ in range(row)]
    dist[start_r][start_c] = 1

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if nr >= row or nr < 0 or nc >= col or nc < 0: continue
            if my_way[nr][nc] == 1: continue
            if dist[nr][nc] != -1: continue

            dist[nr][nc] = dist[r][c] + 1
            if (nr, nc) == (row - 1, col - 1): return dist[nr][nc]

            queue.append((nr, nc))

    return 2000


row, col = map(int, input().split())
my_way = [list(map(int, input())) for _ in range(row)]
closest_dist = 2000

if not any(1 in row for row in my_way):             # 부술 벽이 없으면
    closest_dist = min(move(0, 0), closest_dist)    # 바로 최단거리 찾기

else:   # 부술 벽이 있으면
    for i in range(row):
        for j in range(col):
            if my_way[i][j] == 1:   # 벽을 찾아서
                my_way[i][j] = 0    # 부수고
                closest_dist = min(move(0, 0), closest_dist)    # 이동 (최단거리 갱신)
                my_way[i][j] = 1    # 복원

if closest_dist == 2000: closest_dist = -1
print(closest_dist)
