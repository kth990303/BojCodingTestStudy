function solution(key, lock) {
  const holeCount = lock.reduce((sum, row) => {
      sum += row.reduce((sum, curr) => curr === 0 ? sum + 1 : sum, 0);
      
      return sum;
  }, 0);
  
  
  let degree = 0;
  
  while(degree <= 360) {
      if(check(key, lock, holeCount)) {
          return true;
      }
      
      rotate90(key, key.length);
      degree += 90;
  }
  
  return false;
}

function rotate90(key, size) {
  // 깊은 복사가 아니라 얕은 복사로 카피떠서 여기서 존나 헤맸음
  const temp = key.map((row) => row.map((e) => e));
  
  for(let col = 0; col < size; col++) {
      for(let row = size - 1; row >= 0; row --) {
          key[col][size - row - 1] = temp[row][col];
      }
  }
}

function check(key, lock, holeCount) {
  for(let rowDiff = -1 * (key.length - 1) ; rowDiff < lock.length + key.length - 1 ; rowDiff++) {
      for(let colDiff = -1 * (key.length - 1) ; colDiff < lock.length + key.length - 1 ; colDiff++) {
          if(checkFit(key, lock, rowDiff, colDiff, holeCount)) {
              return true;
          }
      }
  }
  
  return false;
}

function checkFit(key, lock, rowDiff, colDiff, holeCount) {
  let count = 0;
  
  for(let keyRow = 0 ; keyRow < key.length; keyRow++) {
      for(let keyCol = 0 ; keyCol < key.length; keyCol++) {
          const lockRow = keyRow + rowDiff;
          const lockCol = keyCol + colDiff;
          
          if(lock[lockRow] === undefined || lock[lockRow][lockCol] === undefined) {
              continue;
          }
          
          if(key[keyRow][keyCol] === 1) {
              if(lock[lockRow][lockCol] === 1){
                  return false;
              }
              
              count++;
          }
      }
  }
  
  return count === holeCount;
}