# [컨베이어 벨트 위의 로봇]
# 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
# 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

N, K = map(int, input().split())
queue = list(map(int, input().split())) #컨베이어벨트
robot = [0 for i in range(len(queue))] #robot유무

countStep = 0

while True:
    countStep += 1
    # 컨베이어 벨트 & robot 회전
    queue.insert(0, queue.pop())
    robot.insert(0, robot.pop())

    # robot 내리기
    if robot[N-1] == 1:
        robot[N-1] = 0

    # robot move
    for i in range(N - 1, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and queue[i + 1] > 0:
            queue[i + 1] -= 1
            robot[i], robot[i + 1] = robot[i + 1], robot[i]

    if queue.count(0) >= K:
        break

    # robot 내리기
    if robot[N-1] == 1:
        robot[N-1] = 0

    # robot 올리기
    if queue[0] > 0:
        queue[0] -= 1
        robot[0] = 1

    if queue.count(0) >= K:
        break

print(countStep)

