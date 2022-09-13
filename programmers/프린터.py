# https://school.programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
  # enumerate를 이용하여 idx부여 
    priorities = [(v, idx) for idx, v in enumerate(priorities)]
    count = 0
    while True:
        if priorities[0][0] == max(priorities)[0]:
            count += 1
            if priorities[0][1] == location:
                break
            else:
                priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
    return count