# if
x=7
if x>5:
    print(x, "is greater than 5")

# if-else
y=5
if y>0:
    print(y, "is positive")
else:
    print(y,"is negative")

# if elif else
marks=int(input("Enter your marks: "))
if marks<40:
    print("Failed")
elif marks>=40 and marks<= 60:
    print("Grade B")
elif marks>60 and marks<=75:
    print("Grade A")
elif marks>75 and marks<=100:
    print("Grade A+")
else:
    print("Invalid marks")

