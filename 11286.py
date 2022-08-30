import heapq as hq
import sys


# input = sys.stdin.readline # input()사용시 입력시간만으로도 시간초과 
# pq = []
# for _ in range(int(input())):
#     x = int(input())  
#     if x:
#         hq.heappush(pq, (abs(x), x)) # 절대값이 작은것을 Root node에 넣을 거임
#     else:
#       print(hq.heapop(pq)[1] if pq else 0)


import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)