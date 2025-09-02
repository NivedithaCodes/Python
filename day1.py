# Data Type

# 1.Number Type (int,float,complex)

# x=-5
# y=10.5
# z=5+6j
# print(x,type(x))
# print(y,type(y))
# print(z,type(z))

x,y=5,10
print(x,y)
print(x+y)
print("x+y")
# print(x+"y")  type error
print("x"+'y') 
print("x"+"y")
# print(x'+'y)  invalid syntax
# print(x+'+'+'y') type error
print(x,'+',y)
print(str(x)+str(y))

# 2.Text Type (str)

str="Hello"
print(str,type(str))
print(str[0],str[1],str[2],str[3],str[4])
print(str[-1],str[-2],str[-3],str[-4],str[-5])

# 3. Bool Type 
a=True
print(a,type(a))

# 4. None Type 
a=None
print(a,type(a))

# 5.Sequence Type(list,range,tuple)

# fruits=['apple','orange','mango']
# print(fruits,type(fruits))
# print(fruits[1])
# fruits[1]='grapes'
# print(fruits)

fruits=['apple','mango','orange','mango']
print(fruits,type(fruits))
print(fruits[1])
fruits[1]='grapes'
print(fruits)


fruits=['apple',12,'orange','mango']
print(fruits,type(fruits))

for i in range(10):
    print(i,type(i))

for i in range(10):
    print(i,end='')

print("\n")

for i in range(10):
    print(i,end=' ')

print("\n")

for i in range(2,10):
    print(i,end=' ')

print("\n")

for i in range(2,10,2):
    print(i,end=' ')

print("\n")

for i in range(20,10,-2):
    print(i,end=' ')

w = (10,'hello',11)
print(w,type(w))
print(w[2])
# w[2]=3 tuple is immutable ie, not able to change elements
# print(w)

student={"name":"priya",
         "age":32,
         "place":"periya"}

print(student,type(student))
# print(student[0])
print(student["name"])
# mutable
student['name']='Ammu' 
print(student)

set1={1,2,'hello','bye',1}
set2={'hii','hoi','see'}
# it doesnt print 1 as it doesnt retain duplicates
print(set1,type(set1)) 
print(set2,type(set2))
# print(set[2]) indexing not performed

colors=frozenset({'red','blue','yellow'})
print(colors)

x=b"Hello"
print(x,type(x))
print(x[0])
# x[0]=90 immutable
# print(x)

y=bytearray(b'Hello World')
print(y,type(y))
print(y[4])
y[4]=90
print(y)

data=bytearray(b'Hello')
mv=memoryview(data)
print(data,type(data))
print(mv,type(mv))
print(data[1],mv[1])
mv[1]=90
print(mv[1],data[1])
print(data,mv)

print("\n")
name="nivu"
place="kasaragod"
age=21
print(name)
print(place)
print(age)
print(name,place,age)

address="samskrithi,iduvunghal po kalanad 671317 kasaragod kerala"
print(address)

address1 ="samskrithi,iduvunghal"
address2="po kalanad 671317"
address3="kasaragod kerala"
print(address1)
print(address2)
print(address3)

address='''samskrithi,iduvunghal
po kalanad 671317
kasaragod kerala '''
print(address)

print("\n")

address="""samskrithi,iduvunghal
po kalanad 671317
kasaragod kerala """
print(address)

x=[10,'hello',65,'bye',2]
p,q,r,s,t=x
print(x)
print(p)
print(q)
print(r)
print(s)
print(t)

p,q,r,s,t=[10,'hello',65,'bye',2]
print(x)
print(p)
print(q)
print(r)
print(s)
print(t)

# p,q,r,s=[10,'hello',65,'bye',2] 4 variables 5 elements soo too many values to unpack errorp,q,r,s,t=[10,'hello',65,'bye',2]
# p,q,r,s,t,u=[10,'hello',65,'bye',2] 6 variables 5 elements soo too many values to unpack errorp,q,r,s,t=[10,'hello',65,'bye',2]

h=5E3
# 5E3 means 5*10^3 = 5*1000=5000.0
print(h,type(h))

h=5E-3
# 5E-3 means 5*10^-3 = 5*(1/10^3) =5/1000=0.005
print(h,type(h))
 
h=-5E-3
# 5E-3 means -5*10^-3 = -5*(1/10^3) =-5/1000=-0.005
print(h,type(h))

# h=E-3
# print(h)
# gives error E is not defined as it should have number with E

v=1E-5
print(v)

v=2E-5
print(v)

v=1E-10
print(v)

v=2E5
print(v)

# random number generation
import random
print(random.randrange(2,5))

garage=['BMW M4','Nano','Alto 800','Shift','Lamborgini','duke 390','R15','Splendor']
print(garage)
print(len(garage))

length=len(garage)
print(garage[length-1])

print(garage[:])
print(garage[1:])
print(garage[:1])
print(garage[::1])
print(garage[::-1])
print(garage[2:7:2])
print(garage[-4:-1])
print(garage[-1:-7:-1])
print(garage[-8:])
print(garage[-1:])

# garage[3]='porsche 911'
# print(garage)

garage[3:5]=['porsche 911' ,'Audi 48']
print(garage)

garage[3:5]=['porsche 911']
print(garage)

garage.append(6)
print(garage)

garage.insert(1,'punch')
print(garage)

garage.insert(-1,'nexon')
print(garage)

myGarage=[10,17,25]
garage.extend(myGarage)
print(garage)

# PQRST each string is considered as each item in the list.
myGarage='PQRST'
garage.extend(myGarage)
print(garage)

#remove based on item name
garage.remove('R15')
print(garage)

#pop based on index, if no argument passed,popped from last index
garage.pop(2)
print(garage)

garage.pop()
print(garage)

garage.pop()
print(garage)