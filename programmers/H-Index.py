# def solution(citations):
#     for i in range(len(citations)):
#         arr1 = 0
#         arr2 = 0
#         for h in range(len(citations)):
#             if citations[h] >= i+1:
#                 arr1 += 1
#             if citations[h] <= i+1:
#                 arr2 += 1
#         arr = []
#         if arr1 == arr2:
#           return i+1
#     return 0

def solution(citations):
    answer = 0
    citations.sort()
    a = len(citations)
    for i in range(a):
        if citations[i] >= a-i:
            return a-i
    return 0