def solution(p):
    length = len(p)
    countOpen = 0
    countClose = 0
    balance = 0
    
    u=""
    v=""
    
    if length == 0:
        return p
    elif length >= 2:
        for i, c in enumerate(p):
            if c=="(":
                countOpen +=1
            elif c==")":
                countClose +=1
            if countOpen==countClose:
                u = p[:i+1]
                v = p[i+1:length]
                print("u: " + u + " v: " + v)
                break;
                
        for c in u:
            if c =="(":
                balance+=1
            elif c==")":
                balance-=1
            if balance < 0:
                str = "("
                v = solution(v)
                str += v
                str += ")"
                str += reverse(u)
                return str
        v = solution(v)
        return u+v
    
def reverse(p):
    slice = p[1:len(p)-1]
    str =''
    for c in slice:
        if c=="(":
            str+=")"
        else:
            str +="("
    return str
