answer = []
#23점 코드입니다.
def dfs(m,x,y,flag,visitt):
    if flag<=2 and m[y][x] != '1' and m[y][x] != 'X':
        flag += 1
        visitt.append(m[y][x])
        m[y][x] = '1' #방문 표시
        dfs(m,x+1,y,flag,visitt)
        dfs(m,x-1,y,flag,visitt)
        dfs(m,x,y+1,flag,visitt)
        dfs(m,x,y-1,flag,visitt)
        dfs(m,x+1,y+1,flag,visitt)
        dfs(m,x-1,y-1,flag,visitt)
        dfs(m,x-1,y+1,flag,visitt)
        dfs(m,x+1,y-1,flag,visitt)
    return visitt


def solution(places):
    for m in places:
        cnt = 1
        m = list(map(list,m))
        for i,m_x in enumerate(m):
            for ii,m_y in enumerate(m_x) :
                if m_y == 'P':
                    if i<0 or i>4 or ii<0 or ii>4:
                        break
                    else:
                        m_c = m.copy()
                        visittt = dfs(m_c,i,ii,0,[])
                        if visittt.count('P')>=2:
                            cnt = 0
                            break
            if cnt == 0:
                break
        answer.append(cnt)
    return answer