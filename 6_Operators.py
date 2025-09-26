#Arithemetic 
a, b=5,3
print("Additon is ", (a+b))
print("Multiplication is ", (a*b))
print("division is ", (a/b))
print(f"division is {a/b:.2f}")
print("Floor division", (a//b))
print("Power operator", (a**b))\

#Relational Operator
print(a>b)

#logical Operator
print(10>3 and 5>3)
print(10>2 or 3>4)
print(not 0) # True # print(not 1) = false

# bitwise operator works on binary val of the number
print("bitwise and", a&b)
print("bitwise or", a|b)
print("Bitwise not", ~a)  # ~a = -(a+1) formula for bitwise not

# left shift and right shift
print(a<<2)
print(a>>2)

# identity and membership
  #primitive
x1 = 5
x2 = 5
print(x1 is x2) #True // beacause same memory occupy x2 takes reference of x1 
print(x1 is not x2) #false 
print(x1==x2)
  #Non-primitive
l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2) #False
print(l1 is not l2) #True

str1="hello"
str2="hello"
print(str1 == str2) #True
print(str1 is str2) #True
print(str1 is not str2) #False

l3=(1,2,3)
l4=(1,2,3)
print(l3 is l4) #True
print(l3 is not l4) #False




