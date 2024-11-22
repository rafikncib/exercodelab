function descendingOrder(n){
  //c convert n to string
  str = n.toString();
  
  // create an array of string characters 
  // sort DEC then reverse them
  array = str.split('').sort().reverse();
  
  // create a string from the array
  str = array.join('');
  
  // finaly convert str to integer
  return Number.parseInt(str);
}