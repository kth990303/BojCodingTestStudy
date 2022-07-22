from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0 for i in range(n)])
indices = [] # 로봇이 있는 인덱스
count = 0

# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
while belt.count(0)<k:
  count+=1
  # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
  # 벨트 회전
  belt.rotate(1)
  # 마지막 위치에 있는 경우, 로봇 내리기
  if robot[-1]==1:
    robot[-1]=0
    indices.remove(n-1)
  # 로봇 회전
  robot.rotate(1)
  if len(indices)>0:
    # 로봇이 있는 인덱스 값 1씩 증가
    indices = list(map(lambda x: x+1, indices))
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 마지막 위치에 있는 경우 로봇 내리기
    if n-1 in indices:
        robot[-1]=0
        indices.remove(n-1)
    for index in indices:
      # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
      if index<n-1 and robot[index+1]==0 and belt[index+1]>=1:
        robot[index], robot[index+1] = robot[index+1], robot[index]
        belt[index+1]-=1
        indices[indices.index(index)]+=1
   
  # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
  if robot[0]==0 and belt[0]!=0:
    robot[0]=1
    belt[0]-=1
    indices.append(0)

print(count)



