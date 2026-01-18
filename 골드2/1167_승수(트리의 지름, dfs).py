# 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것(지름) 구하기

# dfs 사용하여 트리의 지름을 구하는 함수
def dfs(start):
    # 방문 여부를 기록하는 리스트와 스택 초기화
    visited = [False] * (V + 1)
    stack = [(start, 0)]

    # 시작 정점 방문 처리
    visited[start] = True
    
    # 가장 먼 정점과 그 거리를 기록할 변수 초기화
    farthest_node = start
    max_distance = 0

    # dfs 수행
    while stack:
        # 현재 정점과 그까지의 거리 정보 꺼내기
        node, distance = stack.pop()

        # 가장 먼 정점과 거리 갱신
        if distance > max_distance:
            max_distance = distance
            farthest_node = node

        # 인접한 정점들 탐색
        for neighbor, weight in edges[node]:
            if not visited[neighbor]:
                # 방문 처리
                visited[neighbor] = True
                # 스택에 인접 정점과 누적 거리 정보 추가
                stack.append((neighbor, distance + weight))

    return farthest_node, max_distance


# 트리의 정점의 개수 (2 <= V <= 100,000)
V = int(input())

# 트리의 간선 정보 입력받기
# 정점 번호가 1부터 V까지이므로 V + 1 크기의 리스트 생성
edges = [[] for _ in range(V + 1)]

# V - 1개의 간선 정보 입력
for _ in range(V - 1):
    # 첫 번째 수는 정점 번호, 그 다음은 (연결된 정점, 거리) 쌍이 반복, -1로 끝남
    edge_info = list(map(int, input().split()))
    node1 = edge_info[0]

    # 간선 정보 처리
    for i in range(1, len(edge_info), 2):
        # -1이 나오면 종료
        if edge_info[i] == -1:
            break

        # (연결된 정점, 거리) 쌍을 간선 정보에 추가
        node2 = edge_info[i]
        weight = edge_info[i + 1]
        edges[node1].append((node2, weight))
        edges[node2].append((node1, weight))
        
# 임의의 한 정점에서 가장 먼 정점 찾기
farthest_node, _ = dfs(1)

# 그 정점에서 다시 가장 먼 정점까지의 거리 구하기
_, diameter = dfs(farthest_node)
print(diameter)
