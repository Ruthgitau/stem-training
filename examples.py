fruit={"orange","mango","apple"}
print(fruit)
print(fruit)
print(fruit)


def add(a,b):
    return a+b
result=add(4,6)
print(result)
result_2=add(8,6)
print(result_2)

#function to replace characters in a string
def replace_in(phrase):
    word=" "
    for letter in phrase:
        if letter.lower() in "aeiou":
            
            word = word +"g"
        else:
         word=word+letter
    return word
print(replace_in (input("enter a phrase")))
