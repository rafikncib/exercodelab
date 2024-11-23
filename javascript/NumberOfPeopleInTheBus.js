var number = function(busStops){
  // Calcule the number of People Get In Bus
  numberPeopleGetInBus = busStops.reduce((total,elem)=>total+elem[0],0);
  
  // Calcule the number of People Get Out Bus
  numberPeopleGetOutBus = busStops.reduce((total,elem)=>total+elem[1],0);
  
  
  // return number of people get in the bus minus the number of people get out the bus
  return numberPeopleGetInBus-numberPeopleGetOutBus
}