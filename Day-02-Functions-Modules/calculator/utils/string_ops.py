
# We'll use these functions from other files (like main.py)
def make_upper(text):
    return text.upper 

def make_lower(text):
    return text.lower 

def reverse(text):
    return text[::-1]
# example: abc ... cba 

def count_words(sentence):
     # count how many words in sentence 
    word = sentence.split()
    return len(word)

# for testing 

if __name__ == "__main__":
    print("testing your string_ops file ")


    print(f"reverse('hello')          → {reverse('hello')}")
    print(f"make_upper('pakistan')   → {make_upper('pakistan')}")
    print(f"make_lower('PYTHON')     → {make_lower('PYTHON')}")
    print(f"count_words('my name is ali sadiq ') → {count_words('my name is aali sadiq')}")


