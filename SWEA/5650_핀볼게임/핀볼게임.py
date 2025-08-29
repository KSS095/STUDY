# N * N (5 <= N <= 100) 핀볼 게임판: 정사각형 블록, 4가지 형태의 삼각형 블록, 웜홀, 블랙홀 존재
# 삼각형 블록 번호: 1(좌하), 2(좌상), 3(우상), 4(우하)
# 사각형 블록 번호: 5
# 웜홀 번호: 6 ~ 10 (최대 5쌍), 블랙홀 번호: -1 (최대 5개)

# 핀볼은 블록, 웜홀, 블랙홀을 만나지 않는 한 현재 방향을 유지하며 직진
# 경사면을 만날 시 직각으로 진행방향이 꺾이고, 수평면 혹은 수직면 혹은 벽을 만나면 반대 방향으로
# 웜홀에 빠지면 동일한 숫자를 가진 반대편 웜홀로 빠져 나오고, 진행방향은 유지
# 블랙홀에 빠지면 게임 종료

# 핀볼이 출발 위치로 돌아오거나 블랙홀에 빠지면 게임 종료, 점수는 벽이나 블록에 부딪힌 횟수 (웜홀은 점수 포함 X)
# 게임판 위에서 출발 위치와 진행 방향을 임의로 선정 가능(블록, 웜홀, 블랙홀이 있는 위치에서는 시작 불가)
# 게임에서 얻을 수 있는 점수의 최댓값은?

#     상  하 좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def play_pinball(start_r, start_c, d): # 핀볼 시작
    # 블랙홀이 없으면..
    # if not any(-1 in row for row in pinball_board): return -1

    # 현재 위치와 방향
    nr, nc = start_r, start_c

    score = 0
    visited = set()

    while True:
        # 현재 진행 방향으로 진행 시 다음 위치
        next_r = nr + dr[d]
        next_c = nc + dc[d]

        # 벽에 부딪히는 경우
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
            if next_r < 0 or next_r >= N:  # 위/아래 벽에 부딪힘
                d = 1 - d  # 0 ↔ 1 반전
            elif next_c < 0 or next_c >= N:  # 좌/우 벽에 부딪힘
                d = 5 - d  # 2 ↔ 3 반전
            score += 1
            continue

        # 다음 위치로 이동
        nr, nc = next_r, next_c
        next_pos_info = pinball_board[nr][nc]

        # 시작 위치로 돌아왔다면 종료
        if (nr, nc) == (start_r, start_c): return score

        # 블랙홀에 빠졌다면 종료
        if next_pos_info == -1: return score

        # 빈 공간이면 계속 진행
        if next_pos_info == 0: continue

        # 블록 처리
        if 1 <= next_pos_info <= 5:
            score += 1

            if next_pos_info == 1:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 3
                elif d == 2:
                    d = 0
                elif d == 3:
                    d = 2
            elif next_pos_info == 2:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 2
            elif next_pos_info == 3:
                if d == 0:
                    d = 2
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 1
            elif next_pos_info == 4:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 0
            elif next_pos_info == 5:
                if d == 0 or d == 1:
                    d = 1 - d
                else:
                    d = 5 - d

        # 웜홀에 빠졌다면
        elif 6 <= next_pos_info <= 10:
            # 같은 번호의 다른 웜홀 찾기
            for i in range(N):
                for j in range(N):
                    # 현재 위치가 아닌 다른 웜홀 찾았다면
                    if (i, j) != (nr, nc) and pinball_board[i][j] == next_pos_info:
                        nr, nc = i, j  # 해당 위치로 이동
                        break
                else:
                    continue
                break

        state = (nr, nc, d)
        if state in visited: return score
        visited.add(state)

    return score


import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 핀볼 게임판(정사각형)의 한 변의 길이
    pinball_board = [list(map(int, input().split())) for _ in range(N)]     # 게임판 정보

    max_score = 0   # 얻을 수 있는 최대 점수 저장

    for r in range(N):
        for c in range(N):
            if pinball_board[r][c] == 0: # 빈공간에서 시작
                for i in range(4):  # 모든 방향으로 진행
                    max_score = max(max_score, play_pinball(r, c, i))

    print(f'#{tc} {max_score}')
