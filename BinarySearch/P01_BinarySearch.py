""" 
이진 탐색
정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색
시작점, 끝점, 중간점을 이용하여 탐색 범위 설정

[시간 복잡도]
단계마다 탐색 범위를 2로 나누는 것과 동일
연산 횟수는 logN에 비례
탐색 범위를 절반씩 줄이며 시간 복잡도는 O(logN)을 보장
"""

# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값) 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)    # 인덱스 값에 +1 해서 몇 번째 원소인지 출력