#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#06.자릿수의 합, 직접 구현한 코드

import sys

N = int(sys.stdin.readline())

'''
125 15232 97 자릿수의 합???
8 13 16인디 
아 여기서 마지막인 97의 자연수 합이 16으로 
가장 크니까 97을 출력했구나 이해했으
함수를 쓰라고 하네 코테 공부하면서 함수는 안써봤는데 한번 써볼까
'''

A = list(map(int, sys.stdin.readline().split()))

def digit_sum(x):
    xLen = len(str(x))
    cnt = 0
    k = 0
    for i in range(xLen):
        k = x // (10 ** (xLen - 1 - i))
        cnt += k
        x -= k * (10 ** (xLen - 1 - i))
    return cnt

#자릿수의 합이 가장 큰 A[i]를 출력해야된다
B = [0] * N
for i in range(N):
    B[i] = digit_sum(A[i])

maxI = 0
maxB = -247000000
for i, x in enumerate(B):
    if x > maxB:
        maxB = x
        maxI = i

print(A[maxI])