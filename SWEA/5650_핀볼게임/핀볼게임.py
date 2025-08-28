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


def play_pinball(start_r, start_c, dr, dc): # 핀볼 시작
    # 현재 위치와 방향
    nr, nc = start_r, start_c
    cur_dr, cur_dc = dr, dc

    score = 0

    while True:
        # 현재 진행 방향으로 진행 시 다음 위치
        next_r = nr + cur_dr
        next_c = nc + cur_dc

        # 벽에 부딪히는 경우
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
            cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
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

        # 사각형 블록에 부딪히면
        if next_pos_info == 5:
            cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
            score += 1

        # 삼각형 블록에 부딪히면
        elif next_pos_info == 1:  # 좌하 삼각형 블록
            score += 1
            if cur_dr == -1 or cur_dc == 1:  # 아래에서 올라오거나 왼쪽에서 오른쪽으로
                cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
            else:  # 위에서 내려오거나 오른쪽에서 왼쪽으로
                cur_dr, cur_dc = cur_dc, cur_dr  # 진행 방향 꺾기

        elif next_pos_info == 2:  # 좌상 삼각형 블록
            score += 1
            if cur_dr == 1 or cur_dc == 1:  # 위에서 내려오거나 왼쪽에서 오른쪽으로
                cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
            else:  # 아래에서 올라오거나 오른쪽에서 왼쪽으로
                cur_dr, cur_dc = -cur_dc, -cur_dr  # 진행 방향 꺾기

        elif next_pos_info == 3:  # 우상 삼각형 블록
            score += 1
            if cur_dr == 1 or cur_dc == -1:  # 위에서 내려오거나 오른쪽에서 왼쪽으로
                cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
            else:  # 아래에서 올라오거나 왼쪽에서 오른쪽으로
                cur_dr, cur_dc = cur_dc, cur_dr  # 진행 방향 꺾기

        elif next_pos_info == 4:  # 우하 삼각형 블록
            score += 1
            if cur_dr == -1 or cur_dc == -1:  # 아래에서 올라오거나 오른쪽에서 왼쪽으로
                cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
            else:  # 위에서 내려오거나 왼쪽에서 오른쪽으로
                cur_dr, cur_dc = -cur_dc, -cur_dr  # 진행 방향 꺾기

        # 웜홀에 빠졌다면
        else:
            pair_num = next_pos_info
            # 같은 번호의 다른 웜홀 찾기
            found = False   # 찾았다는 표시
            for i in range(N):
                if found: break # 찾았으면 그만

                for j in range(N):
                    # 현재 위치가 아닌 다른 웜홀 찾았다면
                    if (i, j) != (nr, nc) and pinball_board[i][j] == pair_num:
                        nr, nc = i, j   # 해당 위치로 이동
                        found = True    # 찾음
                        break


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
                    max_score = max(max_score, play_pinball(r, c, dr[i], dc[i]))

    print(f'#{tc} {max_score}')







# # 방향: 상(0) 하(1) 좌(2) 우(3)
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # 블록 반사 규칙 (block_type: 1~5, direction: 0~3)
# # reflect[block][dir] = new_dir
# reflect = {
#     1: [1, 3, 0, 2],  # 좌하
#     2: [3, 0, 1, 2],  # 좌상
#     3: [2, 0, 3, 1],  # 우상
#     4: [1, 2, 3, 0],  # 우하
#     5: [1, 0, 3, 2],  # 사각형 (반대방향)
# }
#
#
# def play_pinball(start_r, start_c, d):
#     r, c = start_r, start_c
#     score = 0
#
#     while True:
#         r += dr[d]
#         c += dc[d]
#
#         # 벽에 부딪힘
#         if r < 0 or r >= N or c < 0 or c >= N:
#             d = (d ^ 1)  # 반대 방향
#             score += 1
#             continue
#
#         cell = board[r][c]
#
#         # 종료 조건
#         if (r, c) == (start_r, start_c) or cell == -1:
#             return score
#
#         # 빈 칸
#         if cell == 0:
#             continue
#
#         # 블록 (1~5)
#         if 1 <= cell <= 5:
#             d = reflect[cell][d]
#             score += 1
#             continue
#
#         # 웜홀 (6~10)
#         if 6 <= cell <= 10:
#             r, c = wormholes[(cell, (r, c))]
#             continue
#
#
# # 입력 처리
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     # 웜홀 좌표 저장
#     worm_dict = {}
#     for i in range(N):
#         for j in range(N):
#             if 6 <= board[i][j] <= 10:
#                 worm_dict.setdefault(board[i][j], []).append((i, j))
#
#     # 웜홀 매핑 딕셔너리 (양방향)
#     wormholes = {}
#     for num, coords in worm_dict.items():
#         a, b = coords
#         wormholes[(num, a)] = b
#         wormholes[(num, b)] = a
#
#     max_score = 0
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == 0:  # 빈칸에서만 시작
#                 for d in range(4):  # 상하좌우
#                     max_score = max(max_score, play_pinball(i, j, d))
#
#     print(f'#{tc} {max_score}')
