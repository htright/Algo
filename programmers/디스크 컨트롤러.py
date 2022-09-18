# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    jobs.sort()
    count, last = 0, -1
    wait = []
    # A가 0초 이후에 주어졌을 수 있다.
    time = jobs[0][0]
    length = len(jobs)
    answer = 0

    while count < length:
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(wait, (t, s))
        if len(wait) > 0:
            last = time
            term, start = heapq.heappop(wait)
            count += 1
            time += term
            answer += (time + - start)
        # wait안에 요소가 없을 시 계속 기다려야한다.
        else:
            time += 1
    return answer // length