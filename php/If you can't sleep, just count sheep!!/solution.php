function countsheep($num){
  $murmur ="";
  for($sheep=1;$sheep <= $num;$sheep++){
    $murmur .= "$sheep sheep...";
    
  }
  return $murmur;
}