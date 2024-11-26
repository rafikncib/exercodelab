function fiboEvenSum(n) {
  // if n = 1 return the sum is 0
  // else if n = 2 return the sum is 2
  if(n==1){
    return 0; 
  }else if(n==2){
    return 2;
  }
  
  // if n >2 
  // we create two variables fib1 and fib2 contains the previous two terms 
  // we create also a variable called sum contains the sum of all even-valued terms,
  // for example for n = 3, the first even value is 2 
  // so sum = 2
  
  let fib1 = 1;
  let fib2 = 2;
  let sum = fib2;

  // we create a while loop that will end if we reach a term > n
  while(fib2 <= n){

    let aux = fib2;
    fib2 = fib2 + fib1;
    fib1 = aux;
    
    if(fib2 % 2 ==0) sum += fib2;
    
  }

  return sum;
}
