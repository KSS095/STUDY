# 포도주 잔이 일렬로 놓여있고, 효주는 다음과 같은 규칙에 따라 포도주를 마시려고 한다.
# 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

# 효주가 마실 수 있는 최대 포도주의 양을 구합시다.

grape_count = int(input())  # 포도주 잔의 개수
grape_amount = list(int(input()) for _ in range(grape_count))   # 각 포도주 잔에 들어있는 포도주의 양

max_eat_amount = 0  # 효주가 먹은 포도주의 양
back_to_back = 0    # 효주가 연속으로 몇 번 마셨는지

# 모든 포도주 순서대로 마셔버리기
for i in range(grape_count):
    if ~~:
        back_to_back += 1   # 현재 포도주를 마신다고 가정

        if back_to_back == 3:   # 3번 연속 마시려고 할 타이밍이라면
            back_to_back = 0    # 초기화 하고
            continue            # 다음 포도주로 이동

        max_eat_amount += grape_amount[i]   # 포도주 마시기

print(max_eat_amount)