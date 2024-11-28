function smallestMult(n) {
  let result = 1;
  for(let i=1;i<=n;i++){
    result = lcm(result,i);
  }
  return result;
}



function gcd(a,b){
  if(b===0){
    return a;
  }else {
    return gcd(b,a%b);
  }

}

function lcm(a,b){
  return Math.abs(a*b)/gcd(a,b);
}