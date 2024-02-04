#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
# 01. 회문 문자열 검사, 강의내용

import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().strip()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print("#%d NO" %(i + 1))
            break
    else:
        print("#%d YES" %(i + 1))


# 더 짧은 버전
import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().strip()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i + 1))
    else:
        print("#%d NO" %(i + 1))

#면접가면 리버스하지말고 직접 구현해보라고 요구함
