from itertools import permutations

heights = [int(input()) for _ in range(9)]
for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
            
        break # 100인 조합이 여러가지 경우가 있더라도 한번만 하고 끝낸다.