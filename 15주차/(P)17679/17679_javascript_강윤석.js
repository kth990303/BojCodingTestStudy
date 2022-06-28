// 입력값 확인 잘해야함. 문자열의 배열이라 문자열을 문자 배열로 한번 풀어줘야지 안그러면 나중에 문자열을 []로 assing 할 때 오류안나면서 문자열 안바뀜
// js는 segfault 없어서 range 체크 안해두 된다는 장점이 있음
// Array(len0).fill(Array(len1)) 하게되면 큰일나는게 len0 * len1 배열이 생기는데 열이 다 같은 배열 참조하는꼴이됨
//
 
function solution(m, n, board) {
  var answer = recursiveCheck(m, n, board.map((s) => Array.from(s)));
  return answer;
}

function recursiveCheck(rowSize, colSize, board) {
  const logBoard = getLogBoard(rowSize, colSize);
  
  for(let r = 0; r < rowSize; r++) {
      for(let c = 0; c < colSize; c++) {
          checkFourBlock(r, c, board, logBoard);
      }
  }
  
  const popCount = logBoard.reduce((acc, col) => {
      return acc + col.reduce((acc, curr) => curr ? acc + 1 : acc, 0);
  }, 0);

  if(popCount === 0) {
      return popCount;
  }
  dragDownBoard(rowSize, colSize, board, logBoard);
  return recursiveCheck(rowSize, colSize, board) + popCount;
}

function checkFourBlock(r, c, board, logBoard) {
  if(
      !isValidCoordinate(r + 1, c, board) ||
      !isValidCoordinate(r, c + 1, board) ||
      !isValidCoordinate(r + 1, c + 1, board)
  ) {
      return;
  }
  
  const block = board[r][c];
  if (
      block === board[r+1][c] &&
      block === board[r][c+1] &&
      block === board[r+1][c+1]
  ) {
      if(block !== "X"){
          logBoard[r][c] = logBoard[r+1][c] = logBoard[r][c + 1] = logBoard[r+1][c+1] = true;
      }
  }
}

function isValidCoordinate(r, c, board) {
  return r >= 0 && c >= 0 && r < board.length && c < board[0].length;
}

function getLogBoard(rowSize, colSize) {
  return Array(rowSize).fill(0).map(m => Array(colSize));
}

function dragDownBoard(rowSize, colSize, board, logBoard) {
  for(let c = 0; c < colSize; c++) {
      const buf = [];
      let r = rowSize - 1;
      
      while(r >= 0) {
          if(!logBoard[r][c]) {
              buf.push(board[r][c]);
          }
          r--;
      }

      buf.reverse();  // Js unshift O(N)이라 뒤집어서 pop 하는게 빠름

      r = rowSize - 1;
      while(buf.length > 0) {
          board[r][c] = buf.pop();
          r--;
      }
      
      while(r >= 0) {
          board[r][c] = "X";
          r--;
      }
  }
}