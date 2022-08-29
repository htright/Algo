T = int(input())
stk = [] # Python에서 Stack은 그냥 List로 가능
isVPS = True
for i in range(T):
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else: 
            if len(stk) > 0: # if stk: 로 써도됨
                stk.pop()
            else:
                isVPS = False
                break

    if len(stk) > 0: # if stk: 로 써도됨
        isVPS = False

    print('YES' if isVPS else 'NO')