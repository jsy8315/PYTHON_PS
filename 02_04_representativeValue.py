#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#대표값
'''
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

#평균 구하기, 소수 첫째자리 반올림? -> round(n,k) : 소수점 k번째까지만 표현, 반올림
sumA = sum(A)
avgA = round(sumA / N)

minD = abs(avgA - A[0])

#절대값? -> abs()
for i in range(1, N):
    if minD > avgA - A[i] > 0:
        minD = A[i] - avgA
        minI = i

    if minD > A[i] - avgA and minD != A[i] - avgA:
        minD = abs(A[i] - avgA)
        minI = i

print(avgA, minI + 1)
##음....모르겠다. 뭔가 더 쉬운 방법이 있을텐데
'''

# 강의 코드
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

sumA = sum(A)
ave = round(sumA / N)

#최소값도 만들자. 보통 표현되는 최대 정수는 2147000000
min = 2147000000

#enumerate함수
for idx, x in enumerate(A):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1


# python의 round는 round_half_even 방식을 택한다. 
# 우리가 보통 생각하는 반올림은 round_half_up 방식
# a = 4.500, round(a)를 하면 4가 나온다. 
# 정확하게 절반에 위치하면, 짝수값으로 근사값을 한다. 따라서 라운드를 쓰면 안된다. 
# 결론 : 
# a = 66.5
# a = a + 0.5
# a = int(a)
# print(a)
