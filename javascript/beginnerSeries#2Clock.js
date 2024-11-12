function past(h, m, s){
  //#Happy Coding! ^_^
  let hoursToMilliseconds = ((h * 60) * 60) * 1000;
  let minutesToMilliseconds = (m * 60) * 1000;
  let secondsToMilliseconds = (s * 1000);
  
  return hoursToMilliseconds + minutesToMilliseconds +secondsToMilliseconds;
}