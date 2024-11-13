function oddOrEven(array) {
   //enter code here
  if(array == []){
    return "even";
  }
  
  let sum=array.reduce((total,element)=>total+element,0);
  if(sum % 2 ==0){
    return "even";
  }  
  return "odd";
}