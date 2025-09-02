# [0][0] 에서 [N-1][N-1] 까지 이동할 때, 잃을 수 있는 최소 금액

import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move_in_cave():
    global min_cost

    cave_cost = [[min_cost] * N for _ in range(N)]
    cost = cave[0][0]

    heap = []
    heapq.heappush(heap, (0, 0, cost))

    while heap:
        r, c, current_cost = heapq.heappop(heap)
        if current_cost > cave_cost[r][c]: continue

        if r == N - 1 and c == N - 1: return current_cost

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                next_cost = current_cost + cave[nr][nc]

                if next_cost < cave_cost[nr][nc]:
                    cave_cost[nr][nc] = next_cost
                    heapq.heappush(heap, (nr, nc, next_cost))

    return cave_cost[N-1][N-1]


problem_number = 1  # 문제 번호

while True:
    N = int(input())
    if N == 0: break    # 0이 입력되면 종료

    cave = [list(map(int, input().split())) for _ in range(N)]  # 현재 동굴의 도둑루피의 크기 정보

    min_cost = 9 * 125 * 125    # 나올 수 있는 최댓값으로 저장

    print(f'Problem {problem_number}: {move_in_cave()}')
    problem_number += 1 # 문제 번호 1 증가
