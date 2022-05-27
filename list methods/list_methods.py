#lists #can add or remove
fruits=["apple","orange","banana"]
fruits_2=["grape","tomato"]
fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)

my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)
fruits_3=fruits + fruits_2
print(fruits_3)

fruits.extend(fruits_2)
print(fruits)

fruits_2.clear()
print(fruits_2)

#tuples #cannot be added or removed
fruits_4=("apples","cherry","banana")
print(fruits_4)
print(fruits_4[1])

new_list=list(fruits_4)
new_list.append("tomato")
fruits_4=tuple(new_list)

#sets #doesnt allow repeated values
fruits_5={"apple","orange","orange","orange"}
print(fruits_5)


other_list=[]
my_list=[2,4,1,7,8,10,12]
for elem in my_list:
    print(elem)
    other_list.append(elem)
print(other_list)

my_list=[2,4,1,7,8,10,12]
other_list=[elem for elem in my_list]
print(other_list)
other_list=[]
my_list=[2,4,1,7,8,10,12]
for elem in my_list:
        if elem % 2 ==0:
                other_list.append(elem)
print(other_list)

