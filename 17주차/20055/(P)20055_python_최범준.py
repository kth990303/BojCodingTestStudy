from collections import deque

# 로봇이 존재하는 자료구조, 벨트의 내구성을 나타내는 자료구조를 두개를 따로 사용
n,k = map(int,input().split())

belt = deque(map(int,input().split()))
robot_existence = deque(list([0]*n)) #로봇은 0~n 에 존재(내리는 위치 때문에)

result = 0

while belt.count(0) < k:
    #한 칸씩 돌리기
    belt.rotate(1) #벨트 돌리기
    robot_existence.rotate(1) #로봇의 위치 이동
    
    robot_existence[-1] = 0 #맨 마지막 로봇이 있는 자리는 내리는 칸이기에 0으로 setting
    
    if sum(robot_existence) > 0 : #로봇이 하나라도 존재하는 경우
        for i in range(n-2,-1,-1):
            if robot_existence[i] == 1 and robot_existence[i+1] == 0 and belt[i+1]>=1: #로봇이 이동할 수 있는지 check
                    robot_existence[i+1] = 1 
                    robot_existence[i] = 0 
                    belt[i+1] -= 1 #내구도 1줄이기
        robot_existence[-1] = 0 #로봇이 한칸씩 이동했으므로 0을 넣어줌으로서 로봇을 내린다.
    
    if robot_existence[0] == 0 and belt[0]>=1: #로봇을 올리는 위치에 올려주는 역할
        robot_existence[0] = 1 
        belt[0] -= 1 #내구도 1줄이기
    
    result += 1 
print(result)