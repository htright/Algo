def solution(s):
    a = []
    for i in s:
        if a[-1:] != [i]:
            a.append(i)
    return a
