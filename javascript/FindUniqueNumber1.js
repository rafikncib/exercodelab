function findUniq(arr) {
  // do magic
  
  
  for( let i=0;i<arr.length;i++){
    count = 0;
    for(let j=0;j<arr.length;j++){
      if(arr[i]==arr[j]){
        count ++;
      }
      if(count == 2){
        break;
      }
    }
    if(count == 1){
      return arr[i];
    }
  }
  
  
}
