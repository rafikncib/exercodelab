function findUniq(arr) {
  // do magic
  let newArr = arr.sort();
  
  return newArr[0]==newArr[1]?newArr[newArr.length-1]:newArr[0];
}