# end 
print("hi", end=' ')
print("Hello")

#sep(seperator)
print(12,5,2025, sep='/')
print(12,5,2025, sep='-')

#concat + use for only strings in python
x1=10
y1=10
sum=x1+y1
print("addition of "+str(x1)+" and "+str(y1)+" is "+str(sum))

#comma
fname="Shital"
print("My name is", fname)

# fstring : are used over commas as we can create seperate string
#That we can use outside of print

sname="sidhesh"
greet=f"Hello {sname}!!"
print(greet)

# Format method
id=101
age=34
print("my id is {} and my age is {}". format(id, age))
# using index
print("my id is {0} and age is {1}".format(id,age))
#using name as placeholder
print("My age is {a} and id is {eid}".format(a=age, eid=id))

#Format specifier
ename="Mohan"
salary=56000.0
print("Name is %s and salary is %.2f"%(ename,salary))
print("Name is %s and salary is %d"%(ename,salary))