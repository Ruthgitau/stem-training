#dictionaries in python
#dictionaries can hold different data types

mydict={
   "book" : "dynamic",
    "publisher" : "longhorn",
    "year" : "2001",
    "authors" :["john,mike,dan"]}
    



#accesssing item
x=mydict["year"]
print(x)

#accessing using get()
y=mydict["year"]
print(y)


#all keys
x=mydict.keys()
print(x)

#all values
x=mydict.values()
print(x)

#printing all items in a dictionaries
x=mydict.items()
print(x)

#checking if keys exists
if "publisher" in mydict:
    print("publisher is one of the keys")
print(len(mydict))
#dictionaries cannot store duplicates






