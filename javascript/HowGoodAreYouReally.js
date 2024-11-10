function betterThanAverage(classPoints, yourPoints) {
  // Your code here
  let classPointsLength = classPoints.length;
  let sum = 0;
  for(let i=0;i<classPointsLength;i++){
    sum += classPoints[i];
  }
  
  let avg = sum / classPointsLength;
  
  if(yourPoints <= avg) 
    return false;
  else
    return true;
}
