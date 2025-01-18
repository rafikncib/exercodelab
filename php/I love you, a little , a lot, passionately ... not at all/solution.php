function how_much_i_love_you(int $nb_petals): string {
  if ($nb_petals == 0) return "";
  $phrases = ['I love you','a little','a lot','passionately','madly','not at all'];
  $mod =$nb_petals%6;
  return $mod == 0 ? $phrases[5] : $phrases[$mod-1];
}