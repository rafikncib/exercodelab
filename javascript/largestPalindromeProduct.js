function largestPalindromeProduct(n) {

  let smallestNDigitNumber = Math.pow(10,n-1);
  let largestNDigitNumber = Math.pow(10,n)-1;
  let largest = 0;

  for(let i=largestNDigitNumber;i>=smallestNDigitNumber;i--){
   for(let j=largestNDigitNumber;j>=smallestNDigitNumber;j--){
     
     if(largest >i*j) break;

     if(isPalindrome(i*j)&&(largest <i*j)){
       largest =i*j;
     }
    } 
  }
  return largest;
}


function isPalindrome(n){
  let ch = n.toString();
  return ch === ch.split("").reverse().join("");
}