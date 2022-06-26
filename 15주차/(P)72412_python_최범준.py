import re

def solution(info, query): 
    # 입력 : info->4가지의 정보, 점수(문자열), query->개발팀이 궁금해하는 문의조건(문자열) / 출력 : 문의조건에 해당하는 사람들의 숫자? (순서대로)
    
    info_count = len(info)
    query_count = len(query)
    
    new_info = []
    new_query = []
    
    #info 새로운 리스트로 정리
    for info_tmp in info :
        info_tmp = info_tmp.split(" ")
        new_info.append(info_tmp)
        

    #query 새로운 리스트로 정리 
    for query_tmp in query :
        tmp_app = []
        split_query = (query_tmp).split(" and ")
        score = re.sub(r'[^0-9]','',split_query[3])
        food = re.sub(r'[^a-z]','', split_query[3])
        
        if re.sub(r'[^a-z]','', split_query[3]) == "":
            food = "-"
            
        for i in range(0,3):
            tmp_app.append(split_query[i])
            
        tmp_app.append(food)
        tmp_app.append(score)
        
        new_query.append(tmp_app)
    
    
        
        
    #숫자 세는 부분
    answer = []
    
    count_cal = 0

    for i in range(0, query_count):
        answer_count = 0
        print("------------------------")
        for j in range(0, info_count):
            count_cal +=1 
            if new_query[i][0] == new_info[j][0] or new_query[i][0] == '-':
                if new_query[i][1] == new_info[j][1] or new_query[i][1] == '-':
                    if new_query[i][2] == new_info[j][2] or new_query[i][2] == '-': 
                        if new_query[i][3] == new_info[j][3] or new_query[i][3] == '-':
                            if int(float(new_query[i][4])) <= int(float(new_info[j][4])):
                                answer_count += 1
                            
        answer.append(answer_count)   
                
    print(answer)
    return answer