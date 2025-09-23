#list - ordered, mutable collection, can store duplicate element
fruits=["apple", "mango", "bannana"]
print(fruits)
print(fruits[0])
#mutable
fruits[0]="Orange"
print(fruits)
print("--------------------------------------------------------")

#Tuple - ordered, immutable collection, can store duplicate element
family=("Father", "Brother", "Sister")
print(family)
print(family[1])
#immutable
# family[0]="Grand Father"
# print(family)
print("--------------------------------------------------------")

#set - unordered, mutable, unique collection - can not store duplicate element, 
data={100,200,300,300}
print(data)
data.add(700)
print(data)
print("--------------------------------------------------------")

#frozenset - immutable version of set