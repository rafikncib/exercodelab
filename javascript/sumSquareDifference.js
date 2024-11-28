function sumSquareDifference(n) {
  return Math.abs(sumSquare(n) - squareSum(n));
}




function sumSquare(n){
  let sum = 0;
  for(let i=1;i<=n;i++){
    sum+=Math.pow(i,2);
  }

  return sum;
}

function squareSum(n){
  let square = 0;
  for(let i=0;i<=n;i++){
    square+=i;
  }

  return Math.pow(square,2);
}