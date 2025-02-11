""" 숫자 카드 게임 
여러 개의 숫자 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
[문제 해결 아이디어]
각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다.
"""

n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 행에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)
    