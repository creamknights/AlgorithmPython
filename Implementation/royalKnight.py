""" 체스판 같은 8 x 8 좌표 평면 (1,1) ~
나이트는 특정 위치에서 다음 2가지 경우로 이동 가능
1. 수평으로 2칸 이동 후 수직으로 1칸 이동
2. 수직으로 2칸 이동 후 수평으로 1칸 이동

나이트의 현재 위치가 문자열로 주어졌을 때 좌표 평면을 벗어나지 않고
나이트가 이동할 수 있는 경우의 수 출력하기 
행 위치 표현 1, 2, 3, ... , 8
열 위치 표현 a, b, c, ... , h
ex. c2에 있을 때 이동 가능 경우의 수는 6가지
"""

# 나이트의 현재 위치 입력 받기
input_data = input()
row = int(input_data[1])
# 문자로 받은 값을 아스키코드로 변환 후 'a'의 아스키코드로 빼준 후 +1로 현재의 열 좌표 정수로 구하기
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 리스트 # 2 * 2 * 2 = 8가지 경우의수
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 count 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 문자를 아스키코드로 반환하는 함수 ord()
ord('a')    # 97