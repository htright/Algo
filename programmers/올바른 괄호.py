'''
def solution(s):
    answer = True
    st = []
    for b in s:
        if b == '(':
            st.append(b)
        elif len(st) and b == ')':
            st.pop()
        else:
            return False
    return False if len(st) else True
    '''

from collections import deque

def solution(s):
    stack = deque()
    for i in s:
        if i == ')' and not stack:
            return False
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
    return True if not stack else False