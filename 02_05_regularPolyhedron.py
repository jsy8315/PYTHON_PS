#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#정다면체, 직접 구현한 코드

import sys

N, M = map(int, sys.stdin.readline().split())

#먼저 1 ~ N, 1 ~ M list 만들기
NL = []
ML = []

for i in range(1, N + 1):
    NL.append(i)

for i in range(1, M + 1):
    ML.append(i)

print(NL)
print(ML)

#전체가 들어갈 list도 만들어야됨
tot = [0] * (N + M)
print(tot)

wTot = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        wTot.append(i + j)
print(wTot)

for idx, x in enumerate(tot):
    for j in range(len(wTot)):
        if idx + 1 == wTot[j]:
            tot[idx] += 1

print(tot)

maxTot = []
maxT = max(tot)
for idx, x in enumerate(tot):
    if maxT == x:
        maxTot.append(idx + 1)

for i in range(len(maxTot)):
    if i != len(maxTot) - 1:
        print(maxTot[i], end= " ")
    else:
        print(maxTot[i])

