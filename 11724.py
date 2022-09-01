import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1 # 양방향이므로 반대 방향인 adj[b][a]도 넣는다.


ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:# 간선 존재시 next
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)