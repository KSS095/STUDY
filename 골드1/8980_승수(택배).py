# 물건 배송하는 트럭이 본부에서 출발, 마을 1 -> 마을 2 -> ... -> 마지막 마을로 가면서 물건을 배송
# 각 마을은 배송할 물건들을 박스에 넣어 보내며, 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다.
# 박스들은 모두 크기가 같다. 트럭에 최대로 실을 수 있는 박스의 개수, 즉 트럭의 용량이 있다.

# 이 트럭 한대를 이용하여 다음의 조건을 모두 만족하면서 최대한 많은 박스들을 배송하려고 한다.
    # 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
    # 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
    # 조건 3: 박스들 중 일부만 배송할 수도 있다.

# 입력: 마을의 개수, 트럭의 용량, 박스 정보의 개수, 박스 정보(보내는 마을번호, 받는 마을번호, 박스 개수)
# 출력: 트럭 한 대로 배송할 수 있는 최대 박스 수


villages, capacity = map(int, input().split())  # 마을의 개수, 트럭의 용량
boxInfo_count = int(input())    # 박스 정보의 개수
boxInfo = []    # 박스 정보 담을 리스트
max_box_count = 0   # 배송할 수 있는 최대 박스 수

for _ in range(boxInfo_count):
    box = list(map(int, input().split())) # 각 박스 정보
    boxInfo.append(box)

boxInfo.sort(key=lambda x: (x[0], -x[2]))
print(boxInfo)

to_villages = {} # 배송 목적지 마을들

# 모든 박스들에 대해서
for i in range(boxInfo_count):
    from_village, to_village, box_count = boxInfo[i][0], boxInfo[i][1], boxInfo[i][2]

    if from_village in to_villages.keys():
        capacity += box_count
        # ??

    if from_village == i + 1:           # 마을에 순서대로 트럭이 도착
        if capacity > box_count:        # 현재 택배를 트럭에 담을 수 있으면
            max_box_count += box_count  # 결과에 추가
            capacity -= box_count       # 트럭 용량 감소

            to_villages[to_village] = box_count

    else: break # 현재 마을에 박스가 더 없으면 다음 반복문으로 가기


# print(max_box_count)