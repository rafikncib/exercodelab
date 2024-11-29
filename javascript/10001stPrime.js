function nthPrime(n) {
  
  let nbr=1;
  let i=0;

  while(i<n){
    nbr++;
    if(isPrime(nbr)){
      
      i++;
    }
    
  }

  return nbr;
}



function isPrime(a){
  if(a<2) return false;
  for(let i= 2;i<=Math.sqrt(a);i++){
    if(a%i==0) return false;
  }
  return true;
}