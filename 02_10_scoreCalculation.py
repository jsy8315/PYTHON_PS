#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#10. 점수 계산

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
S = [0] * N

if A[0] == 1:
    S[0] = 1

for i in range(1, N):
    if A[i - 1] == 0 and A[i] == 1:
        S[i] = 1
    if A[i - 1] == 1 and A[i] == 1:
        S[i] = S[i - 1] + 1

print(sum(S))