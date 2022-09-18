import heapq

def solution(scoville, K):
    length = len(scoville)
    heapq.heapify(scoville)
    answer = 0
    while length >= 2:
        first = heapq.heappop(scoville)
        length -= 1
        # min heap으로 root node가 최솟값이므로 조건 만족
        if first >= K:
            return answer
        # 아닐시 섞어야한다.
        answer += 1
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
    # 최종값
    if heapq.heappop(scoville) >= K:
        return answer
    else:
        return -1