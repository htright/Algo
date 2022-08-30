N, L = map(int, input().split())
coord = [False] * 1001 # 0 ~ 1000 까지
for i in map(int, input().split()):
    coord[i] = True

ans = 0
x = 0 
while x < 1001:
    if coord[x]:
        ans += 1 # 테이프 하나 씀\
        x += L # 테이프 길이 l 만큼은 True여도 적용이 되어지므로 신경쓰지 않아도 된다.
    else:
        x += 1
print(ans)