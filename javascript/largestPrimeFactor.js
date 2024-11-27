function largestPrimeFactor(number) {
  let largetPrimeFactor = 0;
  let factor = 2;
  while(number > 1){
    if(number % factor==0){
      number /= factor;
      largetPrimeFactor=factor;
    }else{
      factor++;
    }
  }
  return largetPrimeFactor;
}


