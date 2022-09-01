def solution(numbers):
    answer = 0
    a = []
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        if b[-1:] != i:
            a.append(i)
    # for i in b:
    #   answer += b    
    return a