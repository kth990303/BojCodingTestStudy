def solution(p):
    return convert(p)

def check(s):
    stk = []
    for i in s:
        if i == "(":
            stk.append("(")
        else:
            if not stk:
                return False
            stk.pop()
    return not stk

def split(s):
    l = r = 0
    if s[0] == "(":
        l += 1
    else: r += 1
    for i in s[1:]:
        if i == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return l + r

def rev(s):
    ret = ""
    for i in s:
        if i == "(":
            ret += ")"
        else:
            ret += "("
    return ret

def convert(s):
    if check(s):
        return s
    idx = split(s)
    u, v = s[:idx], s[idx:]
    print(u, v)
    if check(u):
        return u + convert(v)
    else:
        return "(" + convert(v) + ")" + rev(u[1:-1])
