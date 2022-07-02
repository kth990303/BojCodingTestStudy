def solution(places):
    answer = []
    
    # 각 고사장 별 사람 위치 리스트
    
    one = []
    two = []
    three = []
    four = []
    five = []
    # 실패. 사람들 위치, 파티션 위치를 좌표로 구했지만 그 이후 방법을 모르겠음.
    
    
    # 각 고사장 별 파티션 위치 리스트
    one_p = []
    two_p = []
    three_p = []
    four_p = []
    five_p = []
    
    
    # places[0] 의 사람, 파티션 좌표 구하기
    
    a = places[0]
    
    for i in range(0,5):
        b = list(a[i])
        for j in range(0,5):
            if b[j]=='P':
                one.append([i,j])
            if b[j]=='X':
                one_p.append([i,j])
                
    # places[1] 의 사람, 파티션 좌표 구하기
    
    c = places[0]
    
    for i in range(0,5):
        d = list(c[i])
        for j in range(0,5):
            if d[j]=='P':
                two.append([i,j])
            if d[j]=='X':
                two_p.append([i,j])       
            
    # places[2] 의 사람, 파티션 좌표 구하기
    
    e = places[0]
    
    for i in range(0,5):
        f = list(e[i])
        for j in range(0,5):
            if f[j]=='P':
                three.append([i,j])
            if f[j]=='X':
                three_p.append([i,j])
                
                
    # places[3] 의 사람, 파티션 좌표 구하기
    
    g = places[0]
    
    for i in range(0,5):
        h = list(g[i])
        for j in range(0,5):
            if h[j]=='P':
                four.append([i,j])
            if h[j]=='X':
                four_p.append([i,j])            
    
    # places[4] 의 사람, 파티션 좌표 구하기
    
    q = places[0]
    
    for i in range(0,5):
        w = list(q[i])
        for j in range(0,5):
            if w[j]=='P':
                five.append([i,j])
            if w[j]=='X':
                five_p.append([i,j])
                
    return four_p