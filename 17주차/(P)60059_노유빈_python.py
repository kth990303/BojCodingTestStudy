# 좌표 별로 두가지의 기준으로 나누어서 거리를 계산하는 방식으로 했지만 실패했다.


import math

# 좌표 거리 계산 함수 

def distance(key_loc):
    
    key_dis_1 = []
    for i in range(0,len(key_loc)-1):
        for j in range(i+1,len(key_loc)):
            key_dis_1.append((key_loc[i][0]-key_loc[j][0])**2+(key_loc[i][1]-key_loc[j][1])**2)
    
    return key_dis_1


def solution(key, lock):
    answer = True
    
    # key : 1 , lock : 0 이 만나야 함
    
    # key, lock 좌표 리스트
    
    key_loc_1 = [ ] 
    lock_loc_1 = [ ]
    
    key_loc_2 = [ ]
    lock_loc_2 = [ ]
        
    
    
    
    # key_loc 들에 대입
    
    for i in range(0,len(key)):
        for j in range(0,len(key[0])):
            if key[i][j] == 1 and i>=j:
                key_loc_1.append([i,j])
            if key[i][j] == 1 and i<j:
                key_loc_2.append([i,j])    
                
    # lock_loc 들에 대입
    
    for i in range(0,len(lock)):
        for j in range(0,len(lock[0])):
            if lock[i][j] == 0 and i>=j:
                lock_loc_1.append([i,j])
            if lock[i][j] == 0 and i<j:
                lock_loc_2.append([i,j])          
    
    
    # key, lock 좌표들의 거리 리스트
    
    key_dis_1 = distance(key_loc_1)
    lock_dis_1 = distance(lock_loc_1)
    
    key_dis_2 = distance(key_loc_2)
    lock_dis_2 = distance(lock_loc_2)
    
    
    
    for i in lock_dis_1:
        if i not in key_dis_1:
            return False
        
    for i in lock_dis_2:
        if i not in key_dis_2:
            return False
      
    
    return True