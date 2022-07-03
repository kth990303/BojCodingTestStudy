def checkPerson(places):
    PersonAxis = []
    #'P'자리 모든 좌표 구하기 - PersonAxis
    for row in range(len(places)):
        for col in range(len(places[0])):
            if places[row][col]=='P':
                PersonAxis.append([row, col])
    #하나의 PersonAxis좌표마다 2보다 거리가 작은 좌표 append (열방향으로)
    #result = [[0,0]
    #           [0,4]
    #           [2,1], [2,3]
    #           [2,3], [2,1]
    #           [4,0]
    #           [4,4]]
    result = []
    for [i1, j1] in PersonAxis:
        tmp = []
        tmp.append([i1, j1])
        for [i2, j2] in PersonAxis:
            if abs(i2-i1) + abs(j2-j1) <= 2:
                if i2!=i1 or j2!=j1:
                    tmp.append([i2, j2])   
        result.append(tmp)
    # print(result)
    return result

def manhattan2(places,row):
    #row에 있는 좌표배열 사이에 파티션이 없으면 거리두기 실패 - True
    
    #바로 옆에 사람이 붙어있는 경우 ex) 'XXPPX'
    for p in row:
        [i1, j1] = p[0]
        for [i2, j2] in p:
            if i1 != i2 or j1 != j2:
                if abs(i1-i2) == 1 and abs(j1-j2) != 1: return True
                if abs(i1-i2) != 1 and abs(j1-j2) == 1: return True
    
    #거리가 2인 자리에 사람이 있는 경우 
    #사람간에 X자리가 있는 경우를 다 따져 생각해보기
    for p in row:
        [i1, j1] = p[0]
        for [i2, j2] in p:
            #거리가 2인 자리에 있는 행에 사람이 있는 경우 그 사이에 x가 있는지 확인 ex) 'OPXPX'
            if i1==i2 and j1!=j2 and abs(j1-j2)==2:
                if places[i1][int((j1+j2)/2)] != 'X': 
                    return True
            #거리가 2인 자리에 있는 열에 사람이 있는 경우 그 사이에 x가 있는지 확인 ex) 'OOPXX', 'OXXXX', 'OXPXX'
            if j1==j2 and i1!=i2 and abs(i1-i2)==2:
                if places[int((i1+i2)/2)][j1] != 'X':
                    return True
            #거리가 2인 자리에 있는 대각선에 사람이 있는 경우 확인
            if i1!=i2 and j1!=j2:
                i_tmp = max(i1,i2)
                j_tmp = max(j1,j2)
                if [i_tmp, j_tmp] == [i1, j1] or [i_tmp, j_tmp] == [i2, j2]:
                    if places[max(i1,i2)-1][max(j1,j2)] != 'X':
                        return True
                    if places[max(i1,i2)][max(j1,j2)-1] != 'X':
                        return True
                else:
                    if places[i_tmp][j_tmp] != 'X':
                        return True
                    if places[i_tmp-1][j_tmp-1] != 'X':
                        return True
    return False

def solution(places):
    
    answer = []

    for p in places:
        pAxis = []
        pAxis = checkPerson(p)
        flag = 1
        if len(pAxis) != 0 and manhattan2(p, pAxis):
            flag = 0
        answer.append(flag)
    
    
    return answer
