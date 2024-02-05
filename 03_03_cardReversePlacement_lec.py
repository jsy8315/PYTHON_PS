#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
#03.카드 역배치, 강의내용

import sys

# 파이썬에서의 스와프
# a, b = b, a

a = list(range(21)) #1 ~ 20까지의 인덱스가 생성됨

for _ in range(10):
    s, e = map(int, sys.stdin.readline().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]
        
a.pop(0) #0번 인덱스 pop 진행

for x in a:
    print(x, end = '')