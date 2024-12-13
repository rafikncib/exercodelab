def double_char(s):
    return''.join([char*2 for char in s])
    
string = input("Enter your string ")

newString = double_char(string)

print(f"* {string}      -> {newString}")