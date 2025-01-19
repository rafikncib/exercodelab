function replace(string $s): string {
  $vowel = "/[aeiouAEIOU]/";
  return preg_replace($vowel, "!", $s);
}