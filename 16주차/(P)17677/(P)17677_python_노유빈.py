def solution(str1, str2):
    
    answer = 0
    
    # 알파벳 리스트
    m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # 각 문자열 소문자로 변환 후 리스트에 담기
    a = list(str1.lower())
    b = list(str2.lower())
    
    # 조건 만족하는 값들만 담을 리스트 생성
    final_a = [ ]
    final_b = [ ]
    
    # a 에서 조건 만족 하는 값들만 final에 담기
    
    for i in range(0,len(a)-1):
        if a[i] in m and a[i+1] in m:
            final_a.append(a[i]+a[i+1])
    
    # b 에서 조건 만족 하는 값들만 final에 담기
    
    for i in range(0,len(b)-1):
        if b[i] in m and b[i+1] in m:
            final_b.append(b[i]+b[i+1])
            
    inter = [ ] # 교집합
    outer = final_a+final_b # 합집합
    outer = list(set(outer))
    
    final_inter = [ ]
    final_outer = [ ]
    
    
    
    # 일반 교집합 구하기
    
    for i in range(0,len(final_a)):
        if final_a[i] in final_b:
            inter.append(final_a[i])
    
    # 일반 교집합 중복 제거
    
    inter = list(set(inter))
    
    # 자카드 교집합 구하기
    
    for i in range(0,len(inter)):
        for j in range(min(final_a.count(inter[i]),final_b.count(inter[i]))):
            final_inter.append(inter[i])
    
    
    
    for i in range(0,len(outer)):
        for j in range(max(final_a.count(outer[i]),final_b.count(outer[i]))):
            final_outer.append(outer[i])        
    
    if len(final_outer)==0:
        return 65536
    
    return int((len(final_inter)/len(final_outer))*65536)