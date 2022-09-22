'''
def solution(s):
    a = []
    for i in s:
        if a[-1:] != [i]:
            a.append(i)
    return a
'''
def solution(arr):
    answer = []
    # 처음만 넣고 그 이후부터는 앞 인덱스와 비교하여 append
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if answer[-1] != arr[i]:
                answer.append(arr[i])
    return answer