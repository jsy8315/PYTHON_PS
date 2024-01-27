#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#자릿수의 합, 강의 내용

#몫과 나머지로 처리하기
'''
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x %10
        x = x // 10
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)
'''

#정수를 str처리해서 자리수 합 구해보기, 좀더 파이썬처럼 사용하기
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)