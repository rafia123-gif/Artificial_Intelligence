#program 1:
for i in range(1500,2701):
        if i%7==0 and i%5==0:
                print(i)
#program 2:
#from fahrenheit to celcius
f=float(input("Enter temperature in fahrenheit"))
c=(f-32)*5/9
print("The temperature in celcius is",c)     
#from celcius to fahrenheit          
c=float(input("Enter temperature in celcius"))
f=((c/5)*9)+32     
print("The temperature in fahrenheit is",f) 
#program 3:
count=0
while(count==0):
        n=int(input("Enter your guess here:"))
        for i in range(1,10):
                if i==n:
                        print("Great!YOUR GUESS IS ABSOLUTELY RIGHT.")
                        count=1
                        break
#program 4:
row=5
for i in range(1,row+1):
        for j in range(1,i+1):
                print('*',end=" ")
        print()
# row=4
# for i in range(row,0,-1):
#         for l in range(i):
#                 print("*",end=" ")
#         print()
#another method
r=4
for i in range(1,5):
    for j in range(1,r+1):
        print('*',end=" ")
    r=r-1
    print()           
#program 5:
word=input("Enter word here:")
count=len(word)
new=""
while(count>0):
       new=new+word[count-1]
       count=count-1
print(new)
#program 6:
even=0
odd=0
number=[1,2,3,4,5,6,7,8,9]
for i in number:
       if i%2==0:
              even=even+1
       else:
              odd=odd+1  
print("Even numbers are",even)   
print("odd numbers are",odd) 
#program 7:
datalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V',"section":'A'}]
for i in range(len(datalist)):
    print(datalist[i],end=" ")
    print(type(datalist[i]))
    print()
#program 8:
for i in range(0,7):
        if i==3 or i==6:
            continue
        print(i)        
#program 9:
print('0 1',end=" ")
a=0
b=1
c=a+b
while(c<51):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    #iteration:
for i in range(1,51):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("fizzbuzz")
    else:
        print(i)
#program 10:
list1=[]
row=int(input("Enter rows here"))
col=int(input("Enter columns here"))

for i in range(row):
    list=[]
    for j in range(col):
        list.append(i*j)
    list1.append(list)
print(list1)  
#program 11:
count=0
list=[]
list1=[]
while(count==0):
      word=input("enter your string here:")
      if word=='':
         break
      list.append(word)
for i in range(len(list)):
           list1.append(list[i].lower())
for i in range(len(list1)):
           print(list1[i])
#rogram 12:
list=[]
count=0
while(count==0):
    word=input("Enter 4 digits input and the number must be binary(0 , 1)")
    if word=='':
       break
    list.append(word)
# for i in range(len(list)):
#     print(list)

for i in range(len(list)):
    word=list[i]
    t=0

    if word[0]=='1':
      t=t+8
    if word[1]=='1':
      t=t+4

    if word[2]=='1':
       t=t+2

    if word[3]=='1':
        t=t+1

    if t%5==0:
        print(word)           
#program 13:
letters=0
words=1
digits=0
str=input("Enter your string:")
for i in str:
      if i==' ':
          words=words+1  
      if i>='0' and i<='9':
           digits=digits+1
      if i>='a' and i<='z':
            letters=letters+1
      if i>='A' and i<='Z':
            letters=letters+1
print("letters are:",letters)  
print("words are:",words)  
print("Digits are:",digits)   
#program 14:
p=input("Enter your password:")
l=len(p)
if (l<6 and l>16):
      print("invalid password!Make sure ,the lenght must be between 6 and 16")
count=0
for i in range(len(p)):
      if p[i]>='A' and p[i]<='Z':
           count=1
if count==0:
      print("invalid password!There must be one uppercase chracter")
c=0
for j in range(len(p)):
      if p[j]>='a' and p[j]<='z':
           c=1
if c==0:
      print("invalid password!There must be one lowercase chracter")        
c=0
for j in range(len(p)):
      if p[j]>='0' and p[j]<='9':
           c=1
if c==0:
      print("invalid password!There must be a digit between 0 to 9")       
c=0
for i in range(len(p)):
      if p[i]=='$' or p[i]=='#' or p[i]=='@':
            c=1
if c==0:
      print("invalid password!Make sure,there must be some special chracters.")
else:
      print("Your password is correct!") 
    
           
               
        