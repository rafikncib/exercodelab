function solution(string) {
  let new_string = ""
  for(let char_index = 0;char_index<string.length;char_index++){
    if(string[char_index]>='A' && string[char_index]<='Z'){
      new_string +=" "+string[char_index];
    }else{
      new_string +=string[char_index];
    }
  }
  return new_string;
}