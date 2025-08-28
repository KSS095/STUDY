import sys
sys.stdin = open('sample_input.txt')


def swimming_pool(idx, cost):
    global min_cost

    if idx >= 12:   # 1년 이용 계획을 짰다면
        min_cost = min(min_cost, cost)   # 최소비용 갱신
        return
    if cost > min_cost: return    # 가지치기

    swimming_pool(idx + 1, cost + prices[0] * plan[idx])    # 1일 이용권
    swimming_pool(idx + 1, cost + prices[1])    # 1개월 이용권
    swimming_pool(idx + 3, cost + prices[2])    # 3개월 이용권
    swimming_pool(12, prices[3])    # 1년 이용권


T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_cost = 3000 * 30 * 31  # 나올 수 있는 최대 요금

    swimming_pool(0, 0)     # idx = 0 부터 시작, cost = 0 부터 시작

    print(f'#{tc} {min_cost}')