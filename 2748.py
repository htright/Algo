# https://www.acmicpc.net/problem/2748
cache = [-1] * 91 # 초기값
cache[0] = 0
cache[1] = 1
cnt = 0

def f(n):
    global cnt # 전역변수 수정
    cnt += 1 # 호출시마다 1 증가
    if cache[n] == -1: # cache[0], cache[1] 이외에만 수행
        cache[n] = f(n -1) + f(n - 2)
    return cache[n]

print(f(int(input()))) 
# print(f'cnt: {cnt}')

'''
N = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

for i in range(2, N + 1):
    cache[i] = cache[i-1] + cache[i-2]
print(cache[N])
'''