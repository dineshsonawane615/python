number = range(5)
print(number)
print(list(number))

# for loop
l1=[10,20,30,40]

for ele in l1:
    print(ele)

#range function
print("----------------------------------------------------")
for i in range(1,10,2):
    print(i)
print("Range with negative index")
for i in range(10, 0, -1):
    print(i, end=' ')
print()
print("----------------------------------------------------")

# Tuple
t1=(23,33,43,53)

for ten in t1:
    print(ten)

#dict
d1={"fname":"Alice", "age":23, "city":"Delhi"}
print("\niterating over keys in dict")
for key in d1:
    print(key)

print("iterating over values")
for value in d1.values():
    print(value)

print("Iterating over keys and values")
for key, value in d1.items():
    print(key,"->", value)

# break , Continue Statements
print("Output with break and Continue")
for i in range(1, 6):
    if i==4:
        continue
    else:
        print(i)

# pass statement
# if we want to write empty block, function, class without implementation
# if we dont want syntax error with empty block
# if we want to keep function, class, if, elif block empty for future implemtetion
print("pass statement")
z=9
if z<10:
    pass
else:
    print(z) 