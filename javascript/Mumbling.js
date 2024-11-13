function accum(s) {
	// your code
  let newString = "";
  for(let i=0; i <s.length ;i++){
    newString += s[i].toUpperCase();  
    for(let j=1;j<i+1; j++){
        newString += s[i].toLowerCase();
      }
    if(i< s.length -1)
    newString +="-";
  }
  return newString;
}