def solution(numbers, target):
  answer = 0
  queue = [[numbers[0], 0], [(-1) * numbers[0], 0]]
  #print('초기', queue)
  n = len(numbers)
  while queue:
    temp, idx = queue.pop() # pop(-1)
    idx += 1
    #print(temp, idx)
    if idx < n:
      queue.append([temp + numbers[idx], idx])
      #print('+', queue)
      queue.append([temp - numbers[idx], idx])
      #print('-', queue)
    # idx가 n을 초과하면 모든 숫자에 대해 연산이 종료된 것이다.
    else:
      if temp == target:
        answer += 1
  return answer