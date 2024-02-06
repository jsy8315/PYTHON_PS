#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
#04. 두 리스트 합치기

import sys

N = int(sys.stdin.readline())
NL = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
ML = list(map(int, sys.stdin.readline().split()))

cntL = [0] * (N + M)

for i in range(N):
    cntL[i] = NL[i]

for i in range(M):
    cntL[N + i] = ML[i]

cntL = sorted(cntL)

for i in range(N + M):
    if i != N + M - 1:
        print(cntL[i], end = ' ')
    else:
        print(cntL[i])
