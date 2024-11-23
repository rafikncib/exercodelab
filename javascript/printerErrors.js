function printerError(s) {
  // assign the variable letters with all the good colors variables
   let letters="abcdefghijklm";
  // calculate the number of errors in the string s using for of
  let numberOfErrors = 0;
  for(let char of s){
    if(!letters.includes(char)){
      numberOfErrors ++;
    }
  }
  
  // return the error rate 
  return numberOfErrors +"/"+s.length;
}