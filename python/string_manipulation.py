# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:23:37 2025

@author: Rafik Ncib
"""

"""
Print "Hello, World!" in Python.
"""
print("Hello, World!")

"""
Store "RafikLang" in a variable and print it.
"""
language_name = "RafikLang"
print(language_name)

"""
Concatenate "Hello" and "World!" and print the result.
"""

first_string = "Hello"
second_string = "world!"
print(f"{first_string+' '+second_string}")


"""
Find the length of "Python is fun!".
"""

string = "Python is fun!"
print(string)

"""
Convert "hello" to uppercase.
"""
string = "hello"
print(string.upper())


"""
Convert "PYTHON" to lowercase.
"""

string = "PYTHON"
print(string.lower())

"""
Replace "Java" with "Python" in "I love Java".
"""
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)


"""
Extract "fun" from "Python is fun!"
"""

text = "Python is fun!"

string = "fun"

length_string = len(string)

find_index_string_text = text.find(string)

if(find_index_string_text !=-1):
    extract_string = text[find_index_string_text:find_index_string_text+length_string]
    print(extract_string)

"""
Reverse the string "abcdef"
"""

string = "abcdef"
reversed_string = string[::-1]


"""
Check if "madam" is a palindrome.
"""

string = "madam"
reversed_string = string[::-1]
if(string == reversed_string):
    print(f"{string} is palindrome")
    
    

"""
Find the length of a string.
"""    
string = "hello"
print(f"length of {string} is {len(string)}")


"""
Count occurrences of a substring.
"""

string = "hello , hello hello world Hello hello"
count_string = string.count("hello")
print(f"number of occurrences of hello in \"{string}\" is {count_string} ")


"""
Split a string by space.
"""
string = "hello hello hello hello hello world world world world"
lst_from_string = string.split(" ")


"""
Join a list of strings into one.
"""

lst = ['hello', 'new','followers']
string = ' '.join(lst)


"""
Remove leading and trailing whitespace.
"""

string = "       hello        "
new_string = string.strip()


"""
Find the index of a substring.
"""
string = "hello world!"
index = string.find("Hello")


"""
Remove vowels from a string.
"""
import re
vowels = "aeyuio"
string = "aeyuibcienu"
string = string.strip(vowels)

for vowel in vowels:
    if(string.find(vowel)!=-1):
        string = string.replace(vowel,'')
        

"""
Check if a string starts with a certain substring.
"""

string ="hello World!"
substring = "hello"

if(string.startswith(substring)):
    print(f"this string {string} starts with {substring}")
    
"""
Check if a string ends with a certain substring.
"""
string ="hello World!"
substring = "d!"

if(string.endswith(substring)):
    print(f"this string {string} ends with {substring}")
    
"""
Convert a string to title case(Converts the first character of each word to upper case
).
"""
title_string = string.title()

"""
Extract all digits from a string.

"""

string ="ab12cd_89Azw*"

digits_string = ''

for char in string:
    if(char.isdigit()):
        digits_string +=char


"""
Extract all words from a string.
"""

string ="hello world how are you today_23 !"
ls = re.split('[\W_\d]',string)
new_ls = [elem for elem in ls if(elem)]
print(new_ls)

for x in new_ls:
    print(x)
    
"""
Remove all white spaces from a string.
"""

string = "Rafik Ncib hhh ncib gggg ik"
new_string = string.replace(' ','')


"""
Replace all occurrences of a character in a string
"""

string = "hello world hello Hello world"
new_string = string.replace('hello', 'Hi')


"""Join a list of strings into a single string."""
lst_string = ['Rafik','Ncib']

new_string = ' '.join(lst_string)

"""
Find the index of a character in a string.
"""

string = "hello"
print(string.find("e"))


"""
Check if a string is a valid email address.
"""


"""
Remove the first and last character of a string
"""

string = 'nRafikc'
new_string =string[1:-1]


"""
Find the longest word in a sentence.

"""
string = "Rafik Ncib is a developer"
lst = string.split()
print(max(lst,key=len))


"""
Find the shortest word in a sentence.
"""
print(min(lst,key=len))


"""
Find the first non-repeated character in a string.
"""
from collections import Counter

char_count = Counter(string)

for char in char_count:
    if(char_count[char]==1):
        print(char,'hhh')
        break