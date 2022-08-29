# https://www.acmicpc.net/problem/2164

# 시뮬레이션 문제


from collections import deque

# dq = deque()

# N = int(input())
# for i in range(1, N+1):
#     dq.append(i)

# print(dq)
N = int(input())
dq = deque(range(1, N + 1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())


# 배열로는 시간복잡도에서 탈락
arr = []
for i in range(1, N + 1): # arr = [*range(1, N +1 )] 
    arr.append(i) 
while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))

print(arr.pop())