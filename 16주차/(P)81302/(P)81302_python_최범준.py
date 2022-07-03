def solution(places):
    sec = 1
    answer = []
    
    for room in places:
        tmp = 1
        print("-----%d 번째------" % (sec))
        sec += 1
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    
                    #수직, 수평 방향 맨해튼 거리 2이내에 응시자(P)가 있는 경우 검색
                    for x in range(1,3):
                        if i+x <= 4 and i-x >=0 and j+x <=4 and j-x >= 0:
                            if (room[i+x][j] == 'P' or room[i][j+x]=='P' or room[i-x][j] == 'P' or room[i][j-x] == 'P'):
                                print("1 : (%d, %d) "% (i,j))    
                                tmp = 0
                        # 0,0 일때
                        if (i+x <=4 and j+x <=4) and not(i-x >=0 or j-x >=0) :
                            if room[i+x][j] == 'P' or room[i][j+x] == 'P':
                                print("2 : (%d, %d) "% (i,j))
                                tmp = 0
                        # 4,0 일때
                        if (i-x>=0 or j+x <=4) and not(i+x <=4 or j-x >=0):
                            if room[i-x][j] == 'P' or room[i][j+x] == 'P':
                                print("3: (%d, %d) "% (i,j))
                                tmp = 0
                        # 0,4 일때
                        if (i+x<=4 and j-x >=0) and not(i-x >=0 or j+x <=4):
                            if room[i+x][j] == 'P' or room[i][j-x] == 'P':
                                print("4: (%d, %d) "% (i,j))
                                tmp = 0
                        # 4,4 일때
                        if (i-x >=0 and j-x >=0) and not(i+x<=4 or j+x <=4):
                            if room[i-x][j] == 'P' or room[i][j-x] == 'P':
                                print("5: (%d, %d) "% (i,j))
                                tmp = 0
                        # i,0 일때
                        if (i+x <=4 and j+x <=4 and j-x>=0) and not(i-x >=0) :
                            if room[i+x][j] == 'P' or room[i][j+x] == 'P' or room[i][j-x] == 'P' :
                                print("6: (%d, %d) "% (i,j))
                                tmp = 0
                        # 0,j 일때
                        if (i+x <=4 and j+x <=4 and i-x>=0) and not(j-x >=0) :
                            if room[i+x][j] == 'P' or room[i][j+x] == 'P' or room[i-x][j] == 'P' :
                                print("7: (%d, %d) "% (i,j))
                                tmp = 0
                        # i,4 일때
                        if (j-x >=0 and i-x >=0 and i+x <=4) and not(j+x<=4) :
                            if room[i+x][j] == 'P' or room[i][j-x] == 'P' or room[i-x][j] == 'P' :
                                print("8: (%d, %d) "% (i,j))
                                tmp = 0
                        # 4,j 일때
                        if (j-x >=0 and i-x >=0 and j+x <=4) and not(i+x<=4) :
                            if room[i-x][j] == 'P' or room[i][j-x] == 'P' or room[x][j+x] == 'P' :
                                print("9: (%d, %d) "% (i,j))
                                tmp = 0
                    #대각선 방향 응시자 존재 여부 검사
                    
                    
                    #파티션이 존재하는 경우
                    if i-1 >= 0 and j-1 >=0 and i+1 <=4 and j+1 <=4:
                        if room[i-1][j] == 'X' or room[i+1][j] =='X' or room[i][j+1] == 'X' or room[i][j-1] == 'X' or room[i-1][j-1] == 'X' or room[i+1][j+1] == 'X' or room[i-1][j+1] == 'X' or room[i+1][j-1]:
                            tmp = 1
            
            
        answer.append(tmp)
    return answer