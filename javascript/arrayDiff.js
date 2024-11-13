function arrayDiff(a, b) {
  let newArr = a.filter((elem)=> ! b.includes(elem));
  return newArr;
}