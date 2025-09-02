from collections import deque

#     상  하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_fish(row, col, size):
    queue = deque([(0, row, col)])  # (거리, 행, 열)
    visited = [[False] * N for _ in range(N)]
    # 현재 상어 위치 방문 표시
    visited[row][col] = True

    # 먹을 수 있는 물고기 리스트 (거리, 행, 열)
    # 먹을 수 있는 물고기가 여러 개라면
    # 거리 -> 행(위) -> 열(왼쪽) 순서에 따른 우선순위로 먹을 예정
    # 사실 거리에 대해서는 29번째 줄에서 걸러지기 때문에 행, 열만 따지면 된다
    can_eat_fish = []

    while queue:
        d, r, c = queue.popleft()

        # 현재 위치에 먹을 수 있는 물고기가 있다면
        if space_status[r][c] != 0 and space_status[r][c] < size:
            can_eat_fish.append((d, r, c))  # 후보군에 추가

        # 후보군에 존재하는 최단거리보다 긴 거리에 있는 물고기를 찾았다면 종료
        # 일종의 가지치기?
        if can_eat_fish and can_eat_fish[0][0] < d: break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 공간을 벗어나지 않고 방문하지 않았으며
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 상어 크기보다 물고기 크기가 작거나 같다면
                if space_status[nr][nc] <= size:
                    visited[nr][nc] = True  # 방문
                    queue.append((d + 1, nr, nc))    # 거리 + 1 해서 queue에 저장

    # 먹을 수 있는 물고기 후보군이 없다면 None 반환
    if not can_eat_fish: return None

    # 있다면 정렬
    can_eat_fish.sort()
    # 제일 거리가 가까운 (거리가 같다면 행이 가장 작은,
    # 행도 같으면 열이 가장 작은) 후보군 반환
    return can_eat_fish[0]


N = int(input())    # 공간의 크기
space_status = [list(map(int, input().split())) for _ in range(N)]

shark_row, shark_col = 0, 0     # 상어의 위치를 넣을 변수
time = 0    # 엄마 찾기까지 걸린 시간
eat_count = 0   # 먹은 물고기 수
shark_size = 2  # 상어의 크기

# 공간에서 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if space_status[i][j] == 9:
            shark_row, shark_col = i, j # 상어 위치 저장
            space_status[i][j] = 0      # 상어가 있던 곳은 0으로

# 먹을 물고기가 없을 때까지 반복
while True:
    # 현재 상어 위치에서 가장 가까운 물고기 찾기
    closest_fish = find_fish(shark_row, shark_col, shark_size)

    # 먹을 물고기가 없다면 종료
    if closest_fish is None: break

    # (가까운 물고기 까지의 거리, 물고기의 행, 열)
    dist, fish_row, fish_col = closest_fish

    time += dist    # 이동한 거리만큼 시간 증가
    eat_count += 1  # 물고기 먹어버리기

    shark_row, shark_col = fish_row, fish_col   # 상어 위치를 물고기 위치로 갱신
    space_status[fish_row][fish_col] = 0    # 물고기가 있던 곳은 0으로

    if eat_count == shark_size: # 상어의 크기만큼 물고기를 먹었다면
        shark_size += 1 # 상어의 크기 증가
        eat_count = 0   # 먹은 물고기 수 초기화

print(time)









'''
    N x N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있음
    아기상어와 물고기는 모두 자연수의 크기를 가진다.

    가장 처음에 상어는 2의 크기를 가지고 아기상어는
    1초에 상하좌우로 인접한 한 칸씩 이동한다.

    자신보다 큰 물고기가 있는 칸은 지나갈 수 없다.
    자신보다 작은 물고기만 먹을 수 있다.
    크기가 같은 물고기는 먹을 순 없지만, 지나갈 순 있다.

    상어의 이동방법은 다음과 같다.
    - 더 이상 먹을 수 있는 물고기가 없다면 엄마에게 도움을 요청함
    - 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 감
    - 1개 이상이라면 거리가 가장 가까운 물고기를 먹으러 감.
        - 거리가 가까운 물고기가 여러개라면, 가장 위, 좌측에 있는 물고기를 먹는다.

    아기상어는 자신의 크기 만큼의 물고기를 먹을 때 크기가 1 증가함.
    초기 상태에선 2마리를 먹으면 1증가해 3이 됨.

    -> 공간의 상태가 주어졌을 때, 아기상어가 몇 초 동안 도움을 요청하지 않는지 리턴

    공간의 상태:
        0: 빈 칸
        1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
        9: 아기 상어의 위치
'''

'''
    도움을 요청 할 조건 -> 더 이상 먹을 수 있는 물고기가 없을때
    즉, 공간안에 내 몸 보다 작은 물고기가 없을때.

    초기의 상어 상태는 2이다.
    공간에서 빈칸이 아닌 모든 좌표들을 찾고 물고기의 크기와 좌표값을 저장함.
    물고기의 크기 순으로 정렬해서 현재 상어의 크기와 작으면 먹으러 이동함.
    먹으면서 상어의 크기를 증가시키며 진행하다가 더 이상 먹을 수 없으면 종료

    heap으로 공간 상태를 관리함. (크기, 행, 열)로 관리하면 자동으로 다음 먹이가 주어짐

    이동 방법?
    가장 최단거리로 이동함. 상어는 자기보다 큰 물고기를 만나면 돌아가야 함.
'''
# import heapq
# from collections import deque
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
#
# def baby_shark_move(row, col, shark_row, shark_col, cur_time):
#     global choidan_distance
#     '''
#         bfs를 사용하여 이동
#     '''
#     queue = deque()
#
#     if shark_row == row and shark_col == col:  # 물고기 만나면 break
#         choidan_distance = min(choidan_distance, cur_time)
#         return
#
#     for i in range(4):
#         ny, nx = shark_row + dy[i], shark_col + dx[i]
#         if 0 <= ny < N and 0 <= ny < N:
#             if grid[ny][nx] <= baby_shark[0][0]:  # 아기상어보다 작거나 같으면
#                 baby_shark_move(row, col, ny, nx, cur_time + 1)
#
#
# # 공간의 크기 N
# N = int(input())
#
# # 공간의 상태
# grid = [list(map(int, input().split())) for _ in range(N)]
#
# heap = []
# baby_shark = []
# eat_count = 0
# timer = 0
#
# for i in range(N):
#     for j in range(N):
#         if grid[i][j] != 0 and grid[i][j] != 9:  # 물고기를 만나면 (크기, 행, 열) 순으로 기록함.
#             heapq.heappush(heap, (grid[i][j], i, j))
#         elif grid[i][j] == 9:  # 아기상어 만남
#             baby_shark.append((2, i, j))
#
# while heap:
#     size, row, col = heapq.heappop(heap)  # 가장 작고 좌상단에 있는 물고기
#
#     # print(size, baby_shark)
#     if size > baby_shark[0][0]:  # 현재 가장 작은 물고기가 상어보다 크면 종료
#         break
#
#     choidan_distance = float('inf')  # 최단거리
#     # 상어 이동 로직 함수로 이동 거리 구함.
#     baby_shark_move(row, col, baby_shark[0][1], baby_shark[0][2], 0)
#     # dfs 완료하면 하나 먹은거
#     eat_count += 1
#     # 최단거리 만큼 시간 초 추가
#     timer += choidan_distance
#     # 상어 몸 만큼 먹으면 상어 크기 증가, eat횟수 초기화
#     if eat_count == baby_shark[0][0]: baby_shark[0][0] += 1; eat_count = 0
#     # 다시 다음 물고기로 이동.
#
# print(timer)
