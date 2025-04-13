#while loop
count=0
while(count<3):
    print("hello geek")
    count=count+1
#single statement while block
# count=0
# while(count==0):print("hello geek")
#for in loop(iteration over list)
list=["My","Name","is","Rafia"]
for i in list:
    print(i)
#for in loop(iteration over tuple)
tuple=("We","are","fellows")
for i in tuple:
    print(i)
#for in loop(iteratio over string)
str="Pakistan"
for s in str:
    print(s)
#another method
for s in "Punjab":
    print(s)
#iterating by index of sequences(range)over list
list=["im","rafia"]
for i in range(len(list)):
     print(list[i])
#over string
st="islamabad"
for s in range(len(st)):
    print(st[s])
#loop control statements
#continue
s="grapes"
for x in s:
    if x=='e' or x=='g':
     continue
    print("current letter is",x)
#break
s="grapes"
for x in s:
    if x=='e' or x=='s':
        break
print("current word is",x)
#functions:
def func():
    print("hello")
func()   
#functions with parameters
def f1(food):
    print("My fvt dish is",food)
f1("fish")
f1(30)
#default parameters
def f2(food="biryani"):
    print(food,"is my favourite food")
f2("fish")
f2()
#passing list as parameter
def f3(gulf):
  for i in gulf:
      print(i)
l=["hye","robot"]
f3(l) 
#return values
def f4(a,b):
    return a+b
print(f4(4,7))
d=f4(5,8)
print(d)
print(f4("rafia","basharat"))
#keyword arguments:(key=value)
def f6(child1,child2,child3):
    print("my youngest child is",child3)
f6("jawad","esha","hamza")
f6(child3="jawad",child2="esha",child1="hamza")
#classes:
class student:
    marks=10
#creating objects:
s1=student()
print(s1.marks)
#__init__()-->constructor
class person:
 def __init__(self,name,age):
     self.name=name
     self.age=age
p1=person("rafia",21)
print(p1.name)
print(p1.age)
#accessing by functions:
class person:
 def __init__(self,name,age):
     self.name=name
     self.age=age
 def sum(self,a,b):
    return a+b
p1=person("rafia",21)
print(p1.name)
print(p1.age)
print(p1.sum(2,5))

