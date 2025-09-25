T = int(input())

for tc in range(T):
    w, h = map(int, input().split())

    building = [list(input().split()) for _ in range(h)]
    sanggeun_index = None
    stars_index = []

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                stars_index.append((i, j))

    sanggeun_index = 