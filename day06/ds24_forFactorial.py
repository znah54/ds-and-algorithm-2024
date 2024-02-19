# file : ds24_forFactorial.py
# desc : 반복문으로 팩토리얼 구하기 fact(n)
# n! = 1x2x3x ... x(n-1) x n

n = 1000
factValue = 1
for i in range(10, 0 -1):
    factValu = i
print(f'{n}! = \ {factValue} ')

# 재귀호출 factorial
def factorial(num):
    if num <= 1:return 1
    return num * factorial(num-1)

print(f'{n}! = \ {factorial(n)} ')
# 재귀호출 1000을 하면 RecursionError : maximum recursion depth exceeded 재귀호출 최고 깊이를 초과