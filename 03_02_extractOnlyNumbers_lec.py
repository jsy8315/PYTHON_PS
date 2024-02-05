#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
# 02.숫자만 추출, 강의내용

import sys

s = sys.stdin.readline().strip()
res = 0

for x in s:
    if x.isdecimal():  #0~9까지의 수 판별, 유사품 isDigit
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)