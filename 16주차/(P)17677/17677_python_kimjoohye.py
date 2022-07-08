import math

def changeStr(string):
    #문자열 나누기
    result = [string[i:i+2] for i in range(0, len(string)-1)]
    #특수문자, 공백, 숫자 제거 & 소문자 변환
    addIndex = []
    for i in range(len(result)):
        if result[i].isalpha():
            addIndex.append(i)
    string = []
    if len(addIndex)!=0:
        for i in addIndex:
            string.append(result[i].lower())
    print(string)
    return string
def solution(str1, str2):
    answer = 0
    str1 = changeStr(str1)
    str2 = changeStr(str2)
    
    cnt=0
    tmp_s2 = str2.copy()
    for s1 in str1:
        for s2 in tmp_s2:
            if s1==s2:
                cnt+=1
                tmp_s2.remove(s2)
                break
    #분자 : cnt
    #분모 : add
    add = len(str1)+len(str2)-cnt
    if len(str1)==len(str2)==0:
        answer = 1
    else:
        answer = cnt/add
    print(answer)
    answer = math.trunc(answer*65536)
    return answer
