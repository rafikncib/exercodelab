function highAndLow(numbers){
  // create a new array from numbers string
  let newArr = numbers.split(" ").map((ele)=>Number(ele));
  
  // sort the new array from the highest number to the lowest number
  newArr.sort((a,b)=>b-a);
  
  let lowestNumber = newArr[newArr.length - 1];
  let highestNumber = newArr[0];
  
  // return the string contain the lowestNumber space highestNumber
  return highestNumber + " " + lowestNumber;
  
}