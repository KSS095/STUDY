# 원판의 회전 방법
# 번호가 x의 배수인 원판을 d 방향으로 k칸 회전시킨다. d가 0이면 시계 방향, 1이면 반시계 방향
# 원판에 수가 남았다면, '인접하면서' '수가 같은 것'을 모두 찾는다.
    # 1. 그러한 수가 있다면 원판에서 인접하면서 같은 수를 모두 지운다.
    # 2. 없는 경우 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.

# 원판을 T(1 <= T <= 50) 번 회전시킨 후 원판에 적힌 수의 합 구하기

def rotate_circle(circle, direction, number):
    # rotate에서 인자가 양수: 시계, 음수: 반시계 방향 회전
    if direction == 0: direction = 1
    else: direction = -1

    circle.rotate(direction * (number % 4))   # 회전 횟수만큼 돌려버리기 (4번 회전시키면 원상태이므로 % 4 해주기)


from collections import deque

number_of_circle, number_of_integers, number_of_rotate = map(int, input().split())  # 원판의 수, 정수의 수, 회전 수
circles = list(deque(map(int, input().split())) for _ in range(number_of_circle))   # 원판에 있는 정수들의 정보

# 회전 정보([0]: 회전시킬 원판(배수 원판마다), [1]: 회전시킬 방향, [2]: 회전할 칸 수)
rotate_info = [list(map(int, input().split())) for _ in range(number_of_rotate)]

for idx in range(len(rotate_info)):     # 회전
    target_rotate = rotate_info[idx][0]     # 회전 시킬 원판
    rotate_direction = rotate_info[idx][1]  # 회전 방향
    rotate_number = rotate_info[idx][2]     # 회전 횟수

    for i in range(target_rotate, number_of_circle + 1, target_rotate):   # circle index가 1부터 시작, 배수만큼 건너뛰기
        current_circle = circles[i - 1]     # circles 저장을 0번 index부터 했으므로 1 빼주고 회전시키기
        rotate_circle(current_circle, rotate_direction, rotate_number)  # 회전 시키기

    flag = False    # 지운 숫자가 있는지 체크

    # # 일직선에 같은 숫자가 있는지 확인
    # for j in range(number_of_integers): # 원판에 있는 수에 대해서
    #     for i in range(number_of_circle - 1):   # 모든 원판 탐색 (-1은 인덱스 에러 방지)
    #         current_number = circles[i][j]
    #         next_number = circles[i + 1][j]
    #
    #         if current_number != 0 and current_number == next_number:   # 숫자가 0이 아니고, 바로 윗줄과 수가 같다면
    #             circles[i][j] = 0
    #             flag = True
    #
    # # 양 옆에 같은 숫자가 있는지 확인
    # for

    # 세로 처리
    for j in range(number_of_integers):
        i = 0
        while i < number_of_circle:
            if circles[i][j] == 0:
                i += 1
                continue

            start = i
            num = circles[i][j]
            while i < number_of_circle and circles[i][j] == num:
                i += 1

            if i - start >= 2:
                for k in range(start, i):
                    circles[k][j] = 0
                flag = True

    # 가로 처리 (원형)
    for i in range(number_of_circle):
        for j in range(number_of_integers):
            if circles[i][j] == 0:
                continue

            # 현재 위치에서 시작해서 연속 개수 세기
            count = 1
            num = circles[i][j]

            # 오른쪽으로 확장
            k = (j + 1) % number_of_integers
            while k != j and circles[i][k] == num:
                count += 1
                k = (k + 1) % number_of_integers

            # 2개 이상 연속이면 제거
            if count >= 2:
                for _ in range(count):
                    circles[i][(j + _) % number_of_integers] = 0
                flag = True

    if not flag:    # 지운 숫자가 없다면
        non_zero_count = sum(1 for circle in circles for num in circle if num != 0)
        avg_circles = sum(sum(circle) for circle in circles) / non_zero_count  # 평균 구하기

        # 새로운 리스트를 생성하여 변경된 deque 저장
        new_circles = [
            # 평균보다 크면 -1, 작으면 + 1
            deque(0 if num == 0 else (num - 1 if num > avg_circles else num + 1) for num in circle)
            for circle in circles
        ]

        # 원본 변수에 새로운 리스트 할당
        circles = new_circles

    print(circles)