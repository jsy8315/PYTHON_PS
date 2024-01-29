#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#10. 점수계산, 강의내용

import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

sum = 0
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0