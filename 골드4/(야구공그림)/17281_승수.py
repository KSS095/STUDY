import sys
sys.stdin = open('input.txt')

for _ in range(6):
    inning = int(input())
    inning_result = [list(map(int, input().split())) for _ in range(inning)]
    print(inning_result)

    # print(result)