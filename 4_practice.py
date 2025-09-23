#list 
# Q. Perform lab 1 with user input (use input function).Create one list of colors perform add and remove operation on list of colors
# print the list after every operation
colors=["red","blue", "green"]
print(colors)
colors[0]=("yellow")
print(colors)
colors.remove("yellow")
print(colors)
colors.append("violet")

#Set 
# Q. Create set of numbers, add two new numbers in set, remove one element in set with remove(ele) method
#print the set with print function
numbers={200,300,700,899}
print(numbers)
numbers.add(500)
print(numbers)
numbers.remove(200)
print(numbers)

#tuple
# Q. create one tuple of 5 names convert tuple to list, add two new names convert back that list to tuple print the value
names=("dinesh", "Yash", "Pawan", "Isha", "Prerna")
print(names)
temp = list(names)
temp.append("shakti")
temp.append("vanshika")
names = tuple(temp)
print(names)

#dictionary
# Q. Create dictionary with 3 key and value pairs, access the value using key (use get(key) method) 
# update value of existing key, add new key and value pair in existing dictionary
# print the dictionary after every operation
pairs={"name":"Shree","Age":23 ,"City":"Mumbai"}
print(pairs)
print(f"print age: {pairs["Age"]}")
print(pairs["City"])
pairs["age"]=24
pairs["marks"]=76
print(pairs)