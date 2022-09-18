'''
# 테스트 케이스만 통과됨.. solution([1, 2, 3, 2, 3])
def solution(prices):
    answer = []
    while prices:
        time = 0
        p = prices.pop(0)
        print(prices)
        for i in range(len(prices)):
          if p <= prices[i]:
            time += 1
        answer.append(time)
            
        
    return answer'''

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
                # else에도 왜 answer[i] += 1 적용하는지 이해안됨
            else:
                answer[i] += 1
                break
    return answer


'''
# 생각해보기...
def solution(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        if stack != []:

            while stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
    '''