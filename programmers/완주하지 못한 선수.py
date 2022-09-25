# https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    dic = {}
    answer = ''
    # 완주 정보를 hash_map으로 전환
    for person in completion:
        if person in dic: # 동명이인일시 +1
            dic[person] = dic[person] + 1
        else: # 처음 입력시
            dic[person] = 1
    # participant 리스트를 순회하면서 확인하기
    #print(dic)
    for person2 in participant:
         if person2 not in dic:
        #answer = person
            return person2
      # -1값이 아닌 0으로 되는것은 동명이인 한명이 완주하지 못한 것을 의미한다.
         if dic[person2] == 0:
            return person2   
         dic[person2] = dic[person2] -1
      #print((dic[person2], dic[person2] -1))

    return answer