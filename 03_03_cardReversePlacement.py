#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
#03.카드 역배치(정올 기출)
import sys

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(10):
    ai, bi = map(int, sys.stdin.readline().split())
    B = A
    for j in range(ai - 1):
        A[j] = B[j]
    for j in range(ai - 1, ai - 1 + ((bi - ai + 1) // 2)):
        A[j] = B[ai + bi - 2 - j]
    for j in range(bi):
        A[j] = B[j]

for i in range(20):
    print(A[i], end = ' ')

#역배치가 안됨