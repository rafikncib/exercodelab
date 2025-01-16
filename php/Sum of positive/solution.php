function positive_sum($arr) {
  $sum = 0;
  foreach($arr as $item){
    if($item>0) $sum+=$item;
  }
  
  return $sum;
}