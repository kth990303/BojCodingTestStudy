import numpy as np

#key와 lock의 각각의 요소를 합친 배열의 결과 - answer
#answer의 배열의 요소가 모두 1이 아니면 false
def checklock(answer):
    for i in answer:
        for j in i:
            if j!=1:
                return False
    return True

#lock을 key의 size-1만큼 더해서 확장시킨 배열로 만들고 가장자리부분 0으로 초기화
#key와 lock의 블록이 하나씩, 두개씩, 세개씩, ... 점점 많아지게 겹쳐서 더한 후
#(겹쳐지는 부분이 많아지다가 모든 key요소와 모든 lock의 요소가 합쳐진 다음 다시 겹쳐지는 부분이 줄어듬)
#원래의 lock size에 맞게 배열 slice - checklock함수로 unlock할 수 있는지 확인
def unlock(answerkey, lock):
    N = len(lock)
    M = len(answerkey)
    #확장
    lock = np.pad(lock, (M-1, M-1))
    
    #확장시킨 배열에 key를 오른쪽 아래방향으로 한칸씩 옮겨가면서 더하고 원래의 lock size에 맞게 배열 slice
    newM = N+M-1
    for i in range(newM):
        for j in range(newM):
            resultlock = lock.copy()
            resultlock[i:i+M,j:j+M] = lock[i:i+M,j:j+M] + answerkey[:][:]
            if checklock(resultlock[M-1:M+N-1,M-1:M+N-1]):
                return True
    
    return False
def solution(key, lock):
    #numpy array로 변경
    answerkey = np.array(key)
    lock = np.array(lock)
    
    flag = False
    
    for i in range(4):
        # i*90만큼 key회전 -> 0, 90, 180, 270만 수행
        answerkey = np.rot90(answerkey, i)
        flag = unlock(answerkey, lock)
        if flag == True:
            break
    return flag
