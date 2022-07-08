const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {

  const [beltHalfLength, segmentToDestroy] = input[0].split(" ").map(e => Number(e));
  const belt = input[1].split(" ").map(e => { return { hasRobot: false, durability: Number(e) } });

  console.log(solution(belt, beltHalfLength, segmentToDestroy));
  process.exit();
})

const solution = (belt, beltHalfLength, segmentToDestroy) => {
  const robotPositions = [];

  let brokenBelt = 0;
  let count = 0;

  while (brokenBelt < segmentToDestroy) {

    // 1. 벨트가 로봇과 함께 회전
    rotateBelt(belt);
    robotPositions.forEach((v, i) => {
      if (v === undefined) {
        return;
      }
      
      robotPositions[i] = v + 1 >= beltHalfLength * 2 ? 0 : v + 1;
    })
    
    // 로봇 내리자
    departingRobotIndex = robotPositions.findIndex((rp) => rp === beltHalfLength - 1);
    if (departingRobotIndex > -1) {
      belt[robotPositions[departingRobotIndex]].hasRobot = false;
      robotPositions[departingRobotIndex] = undefined;
    }
    
    // 2. 로봇 이동
    robotPositions.forEach((robotPosition, i) => {
      if (robotPosition === undefined) {
        return;
      }
      
      const nextPosition = robotPosition + 1 >= beltHalfLength * 2 ? 0 : robotPosition + 1;
      
      if (belt[nextPosition].hasRobot || belt[nextPosition].durability === 0) {
        return;
      }
      
      belt[robotPosition].hasRobot = false;
      belt[nextPosition].hasRobot = true;
      belt[nextPosition].durability -= 1;
      
      if (belt[nextPosition].durability === 0) {
        brokenBelt++;
      }
      
      robotPositions[i] = nextPosition;
    })

    // 로봇 내리자
    departingRobotIndex = robotPositions.findIndex((rp) => rp === beltHalfLength - 1);
    if (departingRobotIndex > -1) {
      belt[robotPositions[departingRobotIndex]].hasRobot = false;
      robotPositions[departingRobotIndex] = undefined;
    }
    
    // 3. 로봇 올리기
    if (belt[0].durability > 0 && belt[0].hasRobot === false) {
      belt[0].durability -= 1;
      if (belt[0].durability === 0) {
        brokenBelt++;
      }
      
      belt[0].hasRobot = true;
      robotPositions.push(0);
    }
    
    // console.log(belt);
    // console.log(robotPositions);
    count++;
  }

  return count;
}

const rotateBelt = (belt) => {
  const temp = belt[belt.length - 1];
  for (let i = belt.length - 1; i > 0; i--) {
    belt[i] = belt[i - 1];
  };

  belt[0] = temp;
}