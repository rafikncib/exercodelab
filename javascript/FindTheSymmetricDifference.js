function sym(...args) {
  const set1 = new Set(args[0]);
  for(let i=1;i<args.length;i++){
      const set2 = new Set(args[i]);
      set2.forEach(function(element){
        if(set1.has(element)){
          set1.delete(element)
          }else{
            set1.add(element);
          }
        })
      }
      
  
  return [...set1].sort();
}

sym([1, 2, 3], [5, 2, 1, 4]);