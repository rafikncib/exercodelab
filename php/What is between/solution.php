function between(int $a, int $b): array {
  $tab = [];
  for($i = $a; $i<=$b;$i++){
      $tab[]=$i; 
  }
  return $tab;
}