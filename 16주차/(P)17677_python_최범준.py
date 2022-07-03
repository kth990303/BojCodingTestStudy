import math

def solution(str1, str2):
    answer = 0
    
    len_1 = len(str1)
    len_2 = len(str2)
    
    new_str1 = []
    new_str2 = []
    
    #입력 받은 두 문자열을 새로운 리스트에 문자 두 글자씩 끊어서 새 리스트에 저장하기
    for i in range(len_1):
        if not(i == len_1-1):
            if ("a" <= str1[i].lower() <= "z") and ("a" <= str1[i+1].lower() <= "z"):
                tmp = str1[i] + str1[i+1]
                new_str1.append(tmp.upper())
    
    for i in range(len_2):
        if not(i == len_2-1):
            if ("a" <= str2[i].lower() <= "z") and ("a" <= str2[i+1].lower() <= "z"):
                tmp = str2[i] + str2[i+1]
                new_str2.append(tmp.upper())
               
    print(new_str1)
    print(new_str2)
    print("------------------------------------------")                  
    inter_count = 0
    union_count = 0
    
    flag = 0
    inter = []
    
    #모든 같은 집합을 가졌을 때
    
    count = 0
    for i in range(0, len(new_str1)):
            for j in range(0, len(new_str2)):
                if(new_str1[i] == new_str2[j]):
                    count += 1
    
    if count == len(new_str1) * len(new_str2):
        flag = 1
    
    #두 집합이 공집합일때
    if(len(new_str1) == 0 and len(new_str2) == 0):
        answer = 65536
    elif flag==1:
        
        if len(new_str1) > len(new_str2):
            inter_count = len(new_str2)
            union_count = len(new_str1)
        elif len(new_str1) < len(new_str2):
            inter_count = len(new_str1)
            union_count = len(new_str2)
        else:
            inter_count = union_count = len(new_str1)
        
        answer = (inter_count / union_count) * 65536
    
    else:    
        #교집합 수 구하기
        for i in range(0, len(new_str1)):
            for j in range(0, len(new_str2)):
                if(new_str1[i] == new_str2[j]):
        
                    #중복검사 변수
                    tmp_ct1 = 0
                    tmp_ct2 = 0
                    if len(inter) == 0:
                        inter.append(new_str1[i])
                        break
                    else:
                        #숫자 세기
                        for k in inter:
                            if (new_str1[i] == k):
                                tmp_ct1 += 1
                        
                        for t in range(len(new_str2)):
                            if (new_str1[i] == new_str2[t]):
                                tmp_ct2 += 1
                                        
                        if tmp_ct1 < tmp_ct2:
                            inter.append(new_str1[i])
                                    
        inter_count = len(inter)
        
        #합집합 수 구하기
        union = new_str1 + new_str2
        union_count = len(union) - inter_count
        
        if inter_count != 0 and union_count != 0:
            answer = (inter_count / union_count) * 65536    
        
    return math.trunc(answer)