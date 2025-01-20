function findNeedle($haystack) {
  foreach($haystack as $key => $value){
    if($value === 'needle') return "found the needle at position $key";
  }
  return "no needle found";
}