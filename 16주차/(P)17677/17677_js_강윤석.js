function solution(str1, str2) {
    
  const [ str1Map, str2Map ] = [str1, str2]
  .map(str => get2WordChunks(str))
  .map(chunk => getMapOfArr(chunk));
  
  const dividend = getDividend(str1Map, str2Map);
  const divisor = getDivisor(str1Map, str2Map);
  
  if(dividend === 0 && divisor === 0) {
      return 65536
  }
  
  return Math.floor(65536 * (dividend / divisor))
}

function getMapOfArr(strArr) {
  const map = new Map();
  
  strArr.forEach(str => {
      if(map.has(str) === false) {
          map.set(str, 0);
      }
      
      map.set(str, map.get(str) + 1);
  })
  
  return map;
}

function getDividend(str1Map, str2Map) {
  let count = 0;
  
  for(const [ k, v ] of str1Map) {
      if(str2Map.has(k)) {
          count += Math.min(str2Map.get(k), v)
      }
  }
  
  return count;
}

function getDivisor(str1Map, str2Map) {
  const map = new Map(str1Map);
  
  for(const [ k, v ] of str2Map) {
      if(map.has(k)) {
          map.set(k, Math.max(v, map.get(k)))
      } else {
          map.set(k, v);
      }
  }
  
  return Array.from(map.values()).reduce((acc, curr) => acc + curr, 0);
}

function get2WordChunks(str) {
  return Array.from(str)
          .reduce((acc, curr, index) => {
              if(index === str.length - 1) {
                  return acc;
              }
              
              acc.push(`${curr}${str[index+1]}`);
              return acc;
          }, [])
          .filter((chunk) => isAlpha(chunk[0])&&isAlpha(chunk[1]))
          .map((ch) => ch.toLowerCase())
}

function isAlpha(ch) {
  return (ch >= "a" && ch <= "z") || (ch >= "A" && ch <= "Z");
}