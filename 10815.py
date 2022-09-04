# https://www.acmicpc.net/problem/10815

import sys
from bisect import bisect_left ,bisect_right

input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split()))) # 이분탐색을 위해 정렬
M = int(input())
qry = list(map(int, input().split()))
# 선형탐색으로 찾을 시  BIG(NM)으로 500,000 * 500,000 로 시간초과 발생
# 이분탐색시 M * log(N) 500,000 * log(500,000)
ans = []
for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r - l > 0 else 0)
print(*ans) #리스트형식 ans의 출력 형식 맞추기  
# = print(' '.join(map(str,ans)))

'''
for q in qry:
    l = bisect_left(cards, q)
    if cards[l] == q:
        ans.append(1)
    else:
        ans.append(0)
와 같이 bisect_rihgt를 사용하지 않고도 구할 수 있다.
'''

