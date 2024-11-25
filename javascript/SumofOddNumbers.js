function rowSumOddNumbers(n) {
  let sum = Math.pow(n,2) - (n-1);
  let odd =(sum+2);

  for(let i = 1;i<n;i++){
    sum += odd ;
    odd +=2;

  }

  return sum;
 }