import copy

#     상  우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# cctv 종류마다 감시 가능한 방향
possible_monitor = {
    1: [[0], [1], [2], [3]],    # 한 방향
    2: [[0, 2], [1, 3]],    # 수직 방향
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],    # 직각 방향
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],    # 세 방향
    5: [[0, 1, 2, 3]]   # 모든 방향
}


def cctv(acc_cctv, copy_of_office):
    global min_blind_spot, cctv_info
    count_zero = 0  # 0의 개수(사각지대 개수) 세기

    # 모든 cctv를 조사 했다면
    if acc_cctv == len(cctv_info):
        # 사무실을 순회하며
        for i in range(N):
            for j in range(M):
                if copy_of_office[i][j] == 0:   # 0이라면 사각지대
                    count_zero += 1     # 사각지대 개수 추가
        min_blind_spot = min(min_blind_spot, count_zero)    # 최솟값 갱신

        for row in copy_of_office:
            print(row)
        print()

        return

    r, c, cctv_type = cctv_info[acc_cctv]

    # 현재 cctv 타입의 모든 가능한 패턴 시도
    for pattern in possible_monitor[cctv_type]:
        # 현재 사무실 상태 복사
        new_office = copy.deepcopy(copy_of_office)

        # 현재 cctv 타입의 감시 가능한 위치 탐색
        for direction in pattern:
            nr = r + dr[direction]
            nc = c + dc[direction]

            # 사무실 밖으로 벗어나지 않는다면 반복
            while 0 <= nr < N and 0 <= nc < M:
                if new_office[nr][nc] == 6: break   # 벽이면 중단
                if new_office[nr][nc] == 0:     # 빈 공간이라면
                    new_office[nr][nc] = -1    # 감시 가능하다는 표시
                # 이동 중인 방향으로 계속 이동
                nr += dr[direction]
                nc += dc[direction]

        cctv(acc_cctv + 1, new_office)  # 관찰한 cctv 수 1 증가, 갱신된 사무실 전달


N, M = map(int, input().split()) # N: 사무실의 세로, M: 사무실의 가로
office = [list(map(int, input().split())) for _ in range(N)]

min_blind_spot = N * M  # 나올 수 있는 사각지대의 최댓값으로 설정
cctv_info = []  # 현재 사무실에 있는 cctv 정보 (row, col, cctv 종류)

# 사무실을 조사하면서
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:  # cctv라면
            cctv_info.append((i, j, office[i][j]))  # 삽입

cctv(0, office) # 관찰한 cctv 수, 사무실 정보를 인자로 전달

print(min_blind_spot)
