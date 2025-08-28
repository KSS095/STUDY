#     상  하 좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def play_pinball(start_r, start_c, init_dr, init_dc):  # 핀볼 시작
    # 현재 위치와 방향
    nr, nc = start_r, start_c
    cur_dr, cur_dc = init_dr, init_dc

    score = 0

    # 무한루프 방지: 상태(위치+방향) 추적
    visited = set()

    while True:
        # 현재 상태 체크
        state = (nr, nc, cur_dr, cur_dc)
        if state in visited:
            # 무한루프 감지시 종료
            return score
        visited.add(state)

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
        if (nr, nc) == (start_r, start_c):
            return score

        # 블랙홀에 빠졌다면 종료
        if next_pos_info == -1:
            return score

        # 빈 공간이면 계속 진행
        if next_pos_info == 0:
            continue

        # 사각형 블록에 부딪히면
        if next_pos_info == 5:
            cur_dr, cur_dc = -cur_dr, -cur_dc  # 진행 방향 반대로
            score += 1

        # 삼각형 블록에 부딪히면
        elif next_pos_info == 1:  # 좌하 삼각형 블록
            score += 1
            # 수직면(위쪽)이나 수평면(오른쪽)에 부딪히면 반대방향
            if cur_dr == -1 or cur_dc == 1:
                cur_dr, cur_dc = -cur_dr, -cur_dc
                # 경사면에 부딪히면 직각 반사
            else:
                cur_dr, cur_dc = cur_dc, cur_dr

        elif next_pos_info == 2:  # 좌상 삼각형 블록
            score += 1
            # 수직면(아래쪽)이나 수평면(오른쪽)에 부딪히면 반대방향
            if cur_dr == 1 or cur_dc == 1:
                cur_dr, cur_dc = -cur_dr, -cur_dc
                # 경사면에 부딪히면 직각 반사
            else:
                cur_dr, cur_dc = -cur_dc, -cur_dr

        elif next_pos_info == 3:  # 우상 삼각형 블록
            score += 1
            # 수직면(아래쪽)이나 수평면(왼쪽)에 부딪히면 반대방향
            if cur_dr == 1 or cur_dc == -1:
                cur_dr, cur_dc = -cur_dr, -cur_dc
                # 경사면에 부딪히면 직각 반사
            else:
                cur_dr, cur_dc = cur_dc, cur_dr

        elif next_pos_info == 4:  # 우하 삼각형 블록
            score += 1
            # 수직면(위쪽)이나 수평면(왼쪽)에 부딪히면 반대방향
            if cur_dr == -1 or cur_dc == -1:
                cur_dr, cur_dc = -cur_dr, -cur_dc
                # 경사면에 부딪히면 직각 반사
            else:
                cur_dr, cur_dc = -cur_dc, -cur_dr

                # 웜홀에 빠졌다면 (6~10)
        elif 6 <= next_pos_info <= 10:
            pair_num = next_pos_info
            # 같은 번호의 다른 웜홀 찾기
            for i in range(N):
                for j in range(N):
                    # 현재 위치가 아닌 다른 웜홀 찾았다면
                    if (i, j) != (nr, nc) and pinball_board[i][j] == pair_num:
                        nr, nc = i, j  # 해당 위치로 이동 (방향은 그대로)
                        break
                else:
                    continue
                break


import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 핀볼 게임판(정사각형)의 한 변의 길이
    pinball_board = [list(map(int, input().split())) for _ in range(N)]  # 게임판 정보

    max_score = 0  # 얻을 수 있는 최대 점수 저장
    for r in range(N):
        for c in range(N):
            if pinball_board[r][c] == 0:  # 빈공간에서 시작
                for i in range(4):  # 모든 방향으로 진행
                    score = play_pinball(r, c, dr[i], dc[i])
                    max_score = max(max_score, score)

    print(f'#{tc} {max_score}')