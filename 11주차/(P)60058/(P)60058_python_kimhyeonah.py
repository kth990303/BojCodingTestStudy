#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(p):
    def check(p):
        if p.count('(') == p.count(')'):
            stack = []
            for i in p:
                if i == '(': stack.append(i)
                else:
                    if stack: stack.pop()
                    else: return False
            return len(stack) == 0
    
    if p == '' or check(p): return p
    
    u = p[0]
    v = p[1:]
    
    for i in range(2, len(p)+1):
        if u.count('(') == u.count(')') and v.count('(') == v.count(')'):
            break
        u = p[:i]
        v = p[i:]
    
    if check(u):
        return u + solution(v)
    
    result = '(' + solution(v) + ')'
    u = u[1:-1]
    for i in u:
        if i == '(': result += ')'
        else: result += '('
    
    return result

