#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(n, build_frame):
    def check():
        for x, y, a in answer:
            if a == 0:
                if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer: continue
                else: return True
            else:
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer): continue
                else: return True
        return False
    
    answer = []
    for x, y, a, b, in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if check():
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if check():
                answer.remove([x, y, a])
    
    answer.sort(key = lambda x: (x[0], x[1], x[2]))
    return answer

