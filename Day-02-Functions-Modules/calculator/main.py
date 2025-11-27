# import all the main (thing or function ) from utils folder 

from utils import (
    add, subtract, multiply, divide,
    make_upper, make_lower, reverse, count_words,is_number
)

print(".. my calculator  + text playground ===\n")


# for math 
a = 10 
b = 20 
print("math session")
print(f"{a} + {b} = {add(a , b)}")
print(f"{a} _ {b} = {subtract(a, b)}")
print(f"{a} × {b} = {multiply(a, b)}") 
print(f"{a} ÷ {b} = {divide(a, b)}")


# for text
name = " ali"
sentence = " i'm the student of punjab university lahore"
 
print("text session")
print(f"Name in cap       : {make_upper(name)}")       
print(f"Name in small     : {make_lower(name)}")       
print(f"Reverse name      : {reverse(name)}")        
print(f"Words in sentence : {count_words(sentence)}")


# for output 
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("=== My Calculator + Text Playground Result ===\n\n")
    
    f.write("Math Results:\n")
    f.write(f"{a} + {b} = {add(a, b)}\n")
    f.write(f"{a} - {b} = {subtract(a, b)}\n")
    f.write(f"{a} × {b} = {multiply(a, b)}\n")
    f.write(f"{a} ÷ {b} = {divide(a, b)}\n\n")
    
    f.write("Text Results:\n")
    f.write(f"Name in CAPS      : {make_upper(name)}\n")
    f.write(f"Name in small     : {make_lower(name)}\n")
    f.write(f"Reversed name     : {reverse(name)}\n")
    f.write(f"Total words       : {count_words(sentence)}\n\n")