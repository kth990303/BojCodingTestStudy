def solution(key, lock):
    N = len(lock); M = len(key)
    
    def isValidState(y_offset, x_offset):
        for i in range(N):
            for j in range(N):
                if (0 <= i + y_offset < M and 0 <= j + x_offset < M): 
                    if key[i+y_offset][j+x_offset] + lock[i][j] != 1: # 키의 오프셋 합 좌표가 자물쇠 내부에 있을 때
                        return False
                elif not lock[i][j]: return False # 키의 오프셋 합 좌표가 밖에 있으면 자물쇠만 보면 됨
        return True

    flag = False
    for i in range(4):
        flag |= any([isValidState(i, j) for i in range(-N+1, N) for j in range(-N+1, N)])
        key = list(zip(*key[::-1])) # 키 회전
    return flag
