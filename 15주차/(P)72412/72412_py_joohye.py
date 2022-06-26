def check(string, info, num):
    arr = []
    if(string == '-'):
        return info
    #숫자 비교
    if num == 4:
        query_number = int(string)
        for i in info:
            info_number = int(i[4])
            if query_number <= info_number:
                arr.append(i)
        return arr
    #문자열 비교
    for i in info:
        if i[num]==string:
            arr.append(i)
    return arr

def solution(info, query):
    #info에 있는 지원자 분리하기
    info_tmp = []
    for i in info:
        tmp = i.split(" ")
        info_tmp.append(tmp)
    info = info_tmp
    #query에 있는 것도 'and ' 제외하고 info처럼 분리
    query_tmp = []
    
    for i in query:
        tmp = i.replace("and ", "")
        query_tmp.append(tmp)
    query = []
    for i in query_tmp:
        tmp = i.split(" ")
        query.append(tmp)
    
    #비교
    answer = []
    for i in query:
        arr = check(i[0], info, 0)
        arr = check(i[1], arr, 1)
        arr = check(i[2], arr, 2)
        arr = check(i[3], arr, 3)
        arr = check(i[4], arr, 4)
        answer.append(len(arr))

    return answer
