# A(i)는 A(i-1)의 배수라는 조건이 있으므로 Greedy 적용가능하다.

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K // coin
    K %= coin 
print(ans)