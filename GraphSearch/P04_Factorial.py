""" 
팩토리얼
n! = 1 x 2 x 3 x ... x (n-1) x n
수학적으로 0!과 1!의 값은 1이다.
"""

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<= 1:    # [종료 조건] n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!을 그대로 코드로 작성
    return n * factorial_iterative(n-1)

print('반복적 구현:', factorial_iterative(5))    # 120
print('재귀적 구현:', factorial_recursive(5))    # 120