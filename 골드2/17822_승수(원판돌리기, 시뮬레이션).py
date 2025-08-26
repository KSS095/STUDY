# # 원판의 회전 방법
# # 번호가 x의 배수인 원판을 d 방향으로 k칸 회전시킨다. d가 0이면 시계 방향, 1이면 반시계 방향
# # 원판에 수가 남았다면, '인접하면서' '수가 같은 것'을 모두 찾는다.
#     # 1. 그러한 수가 있다면 원판에서 인접하면서 같은 수를 모두 지운다.
#     # 2. 없는 경우 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
#
# # 원판을 T(1 <= T <= 50) 번 회전시킨 후 원판에 적힌 수의 합 구하기
from collections import deque


def rotate_circle(circle, direction, number):
    # rotate 에서 인자가 +: 시계, -: 반시계 방향 회전
    if direction == 0: direction = 1
    else: direction = -1

    circle.rotate(direction * number)   # 회전 횟수만큼 돌려버리기 (4번 회전시키면 원상태이므로 % 4 해주기)


def remove_adjacent(circles, n_circles, n_integers):
    removed = False
    to_remove = set()

    for i in range(n_circles):
        for j in range(n_integers):
            if circles[i][j] == 0:
                continue
            current = circles[i][j]

            # 같은 원판 내 인접 (좌/우)
            left = (j - 1) % n_integers
            right = (j + 1) % n_integers
            if circles[i][left] == current:
                to_remove.add((i, j))
                to_remove.add((i, left))
                removed = True
            if circles[i][right] == current:
                to_remove.add((i, j))
                to_remove.add((i, right))
                removed = True

            # 위/아래 원판 같은 j 인덱스
            if i > 0 and circles[i - 1][j] == current:
                to_remove.add((i, j))
                to_remove.add((i - 1, j))
                removed = True
            if i < n_circles - 1 and circles[i + 1][j] == current:
                to_remove.add((i, j))
                to_remove.add((i + 1, j))
                removed = True

    # 지우기
    for i, j in to_remove:
        circles[i][j] = 0

    return removed


number_of_circles, number_of_integers, number_of_rotates = map(int, input().split())  # 원판의 수, 정수의 수, 회전 수
circles = list(deque(map(int, input().split())) for _ in range(number_of_circles))   # 원판에 있는 정수들의 정보

# 회전 정보([0]: 회전시킬 원판(배수 원판마다), [1]: 회전시킬 방향, [2]: 회전할 칸 수)
rotate_info = [list(map(int, input().split())) for _ in range(number_of_rotates)]

for idx in range(len(rotate_info)):     # 원판 회전
    target_rotate = rotate_info[idx][0]     # 회전 시킬 원판
    rotate_direction = rotate_info[idx][1]  # 회전 방향
    rotate_number = rotate_info[idx][2]     # 회전 횟수

    for i in range(target_rotate - 1, number_of_circles, target_rotate):   # circle index가 1부터 시작, 배수만큼 건너뛰기
        rotate_circle(circles[i], rotate_direction, rotate_number)  # 회전 시키기

    # 인접한 숫자 제거(제거한 숫자 없으면 False 반환)
    is_removed = remove_adjacent(circles, number_of_circles, number_of_integers)

    if not is_removed:    # 제거한 숫자가 없다면
        total_sum = sum(sum(circle) for circle in circles)
        non_zero_count = sum(num != 0 for circle in circles for num in circle)

        if non_zero_count > 0:
            avg_val = total_sum / non_zero_count
            for i in range(number_of_circles):
                for j in range(number_of_integers):
                    if circles[i][j] != 0:
                        if circles[i][j] > avg_val:
                            circles[i][j] -= 1
                        elif circles[i][j] < avg_val:
                            circles[i][j] += 1

    print(circles)
circle_sum = sum(sum(circle) for circle in circles)
print(circle_sum)