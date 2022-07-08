function solution(places) {
  return places.map((p) => {
      const place = p.map((str) => Array.from(str));
      
      console.log(place) //log
     
     for(let row = 0; row < place.length; row++) {
      for(let col = 0; col < place[0].length; col++) {
          if(place[row][col] !== "P") {
              continue;
          }
          
          if(isDistanceOK(place, row, col) === false) {
              console.log(`Not ok at [${row},${col}]`)    //log
              return 0;
          }
      }
  }
      return 1;
  });
}

const manhatan1 = [[0,1], [1,0], [0,-1], [-1,0]];
const manhatan2 = [[1,1], [1,-1], [-1,1], [-1,-1]];
const manhatan2Far = [[0, 2], [2,0], [-2,0], [0,-2]];

function isDistanceOK(places, row, col) {
  console.log(`Person at [${row},${col}]`)    //log
  
  const manhatan1People = manhatan1.filter(([r, c]) => {
      const nr = row + r;
      const nc = col + c;
      
      return isPosValid(places, nr, nc) && places[nr][nc] === "P";
  })
  
  if(manhatan1People.length > 0) {
      return false;
  }
  
  const manhatan2People = manhatan2.filter(([r, c]) => {
      const nr = row + r;
      const nc = col + c;
      
      return isPosValid(places, nr, nc) && places[nr][nc] === "P";
  });
  
  if(manhatan2People.length > 0) {
      for(const [r, c] of manhatan2People) {
          if(places[row][col + c] !== "X" || places[r + row][col] !== "X") {
              return false;
          }
      }
  }
  
  const manhatan2FarPeople = manhatan2Far.filter(([r, c]) => {
      const nr = row + r;
      const nc = col + c;
      
      return isPosValid(places, nr, nc) && places[nr][nc] === "P";
  });
  
  if(manhatan2FarPeople.length === 0) {
      return true;
  }
  
  for(const [r, c] of manhatan2FarPeople) {
      if(r === 0 && places[row][col + c/2] !== "X") {
          return false;
      }
      
      if(c === 0 && places[row + r/2][col] !== "X") {
          
          return false;
      }
  }
  
  return true;
}

function isPosValid(places, row, col) {
  return places[row] && places[row][col];
}