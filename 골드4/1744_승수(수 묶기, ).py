# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하기
# 단, 수열의 두 수를 묶고, 수열의 합을 구할 때 묶은 수는 서로 곱한 후 더함

# 수열이 주어졌을 때, 수열의 합의 최댓값을 구하자

N = int(input())
numbers = [int(input()) for _ in range(N)]

result = 0

# 곱셈이 있기 때문에 양수, 음수로 나눠서 처리
positive = []
negative = []

# 정렬하고 양수 음수 나누려고 했는데 
# 그냥 나누는게 더 편한듯?

# N이 50보다 작으므로 나누는데는 얼마 안걸림
for num in numbers:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

# 양수 처리
# 큰 수 끼리 묶어야 최대가 됨 (내림차순 정렬)
positive.sort(reverse=True)

while len(positive) > 1:
    # 큰 수 두 개씩 묶기
    a = positive.pop(0)
    b = positive.pop(0)
    
    # 1이 포함된 경우는 곱셈보다 덧셈이 더 큼
    if a == 1 or b == 1:
        result += a + b
    else: # 그 외의 경우 곱셈이 더 큼
        result += a * b

# 남은 수가 있으면 더해주기
if len(positive) == 1:
    result += positive.pop()


# 음수와 0 처리
# 작은 수 끼리 묶어야 최대가 됨 (오름차순 정렬)
negative.sort()
while len(negative) > 1:
    # 작은 수 두 개씩 묶기
    a = negative.pop(0)
    b = negative.pop(0)
    # 음수 끼리 곱하면 양수가 되므로 무조건 곱셈
    result += a * b

# 남은 수가 있으면 더해주기
if len(negative) == 1:
    result += negative.pop()


print(result)
