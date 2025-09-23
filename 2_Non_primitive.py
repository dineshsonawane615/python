#list - ordered, mutable collection, can store duplicate element , dynamic array
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
f1=frozenset([500,600,700])
print(f1)
#immutable set
#f1.add(200)
print("--------------------------------------------------------")

# dictionary
person={"fname":"Sid", "age":21}
print(person)

#accessing single value
print("person name is {person[""fname]}") 
print(person["age"])

person["city"]="pune"
print(person)
