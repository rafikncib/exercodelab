function XO(str) {
    //code here
  let newArr = str.split("");
  let sumX = newArr.filter(elem=>elem.toLowerCase()=="x" ).reduce((total,elem)=> total+1,0);
  let sumO = newArr.filter(elem=>elem.toLowerCase()=="o").reduce((total,elem)=> total+1,0);
  return sumX==sumO ?true :false;
}