function specialPythagoreanTriplet(n) {
 let sumOfabc = n;
  
  for(let a=1;a<n/2;a++){
    for(let b=a+1;b<n/2;b++){
      let c = sumOfabc-a-b;
      
        if((Math.pow(a,2)+Math.pow(b,2)===Math.pow(c,2))){
          console.log(n,a,b,c)
          return a*b*c;
        }
      
    }
  }
 return -1;
}
