function feast($beast, $dish){
  if ($beast[0] !== $dish[0] || $beast[-1] !== $dish[-1]){
    return false;
  }
  return true;
}