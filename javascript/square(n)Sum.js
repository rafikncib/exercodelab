function squareSum(numbers){
  let newArr = numbers.map((element)=>element * element);
  return newArr.reduce((total,element)=>total+element,0);
}