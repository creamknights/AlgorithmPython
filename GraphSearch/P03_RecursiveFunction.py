""" 
재귀함수(Recursive Function)
자기 자신을 다시 호출하는 함수
재귀 함수의 종료 조건을 반드시 명시해야 한다.
stack frame에 저장
"""

def recursive_function(i):
    # 100번 째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 3:
        print(i, '번째 재귀 함수는 종료 조건에 해당하므로 다음 함수를 호출하지 않습니다.')
        return
    print(i, '번째 재귀 함수에서', i + 1,  '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

"""
1 번째 재귀 함수에서 2 번째 재귀 함수를 호출합니다.
2 번째 재귀 함수에서 3 번째 재귀 함수를 호출합니다.
3 번째 재귀 함수는 종료 조건에 해당하므로 다음 함수를 호출하지 않습니다.
2 번째 재귀 함수를 종료합니다.
1 번째 재귀 함수를 종료합니다.
"""