function primeSummation(n) {

  if(n<2){
    return 0;
  }

  
  let primeArray = Array(n).fill(true);
  
  primeArray[0] = primeArray[1] = false;
  
  for(let i=2;i<=Math.sqrt(n);i++){
    if(isPrime(i)){
      for(let j=i*i;j<n;j+=i){
        primeArray[j] = false;
      }
      
    }
  }

  let sum = 0;
  for(let i=0;i<n;i++){
    if(primeArray[i]){
      sum+=i;
    }
  }
  
  return sum;
}

primeSummation(2000000);


// verif if a number is prime
function isPrime(num){
  for(let i = 2;i<=Math.sqrt(num);i++){
    if(num%i === 0){
      return false;
    }
  }

  return true;
}