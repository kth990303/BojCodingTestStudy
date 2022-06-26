# 집합을 활용한 1번 방식으로 풀었다가 효율성 테스트에서 통과 못해서
# 배열의 인덱스에 1대1 대응시켜 푸는 방식을 생각해서 2번으로 풀었습니다.
# 근데 2번도 효율성 통과 못해서 리뷰 부탁드립니다ㅠ

#1
## from collections import defaultdict
## def solution(info, query):
##    info = [row.split() for row in info]
##    query = [row.split(" and ") for row in query]
##    for row in query:
##        temp = row[-1].split()
##        temp[-1] = int(temp[-1])
##        row.pop(-1)
##        row += temp
##    infos = defaultdict(list)
##
##    for i, row in enumerate(info):
##        infos[row[0]] +=[i]
##        infos[row[1]] +=[i]
##        infos[row[2]] +=[i]
##        infos[row[3]] +=[i]
##    infos['-'] += range(len(info))
##
##    answer = []
##    for a,b,c,d,e in query:
##        result = list(set(infos[a]) & set(infos[b]) & set(infos[c]) & set(infos[d]))
##        result = [index for index in result if int(info[index][-1]) >= e]
##        answer.append(len(result))
##            
##    return answer

#2
from collections import defaultdict
def decoder(key):
    a = int(key/8)
    b = int(key%8/4)
    c = int(((key%8)%4)/2)
    d = ((key%8)%4)%2
    return (a,b,c,d)

def solution(info, query):
    hashedList = defaultdict(list)
    query = [row.split(" and ") for row in query]
    for row in query:
        temp = row[-1].split()
        temp[-1] = int(temp[-1])
        row.pop(-1)
        row += temp
        
    info = [row.split() for row in info]
    lang = ["cpp", "java", "python"]
    position = ["backend", "frontend"]
    worked = ["junior", "senior"]
    food = ["chicken", "pizza"]
    inputList = [lang, position, worked, food]
    
    
    for i, row in enumerate(info):
        hashIndex = inputList[0].index(row[0])*8+ inputList[1].index(row[1])*4+ inputList[2].index(row[2])*2+ inputList[3].index(row[3])
        hashedList[hashIndex] += [i] 
    
    answer = []
    keyList = list(hashedList.keys())
    
    
    for row in query:
        count = 0
        term = []
        for j in range(len(row)-1):
            if row[j]!= "-":
                term.append(j)
        for key in keyList:
            decoded = decoder(key)
            flag= True
            for x in term:
                if decoded[x] != inputList[x].index(row[x]):
                    flag=False
                    break
            if flag:
                for item in hashedList[key]:
                    if int(info[item][-1]) >= int(row[-1]):
                        count +=1
        answer.append(count)
        
            
    return answer
