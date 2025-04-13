# implementing stack
class stack:
    def __init__(self):
        self.list=[]
    def push(self,x):
        self.list=[x]+self.list
    def pop(self):
        # if!self.is_empty():
        return self.list.pop(0)
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.list)
print(s1.pop())
# implementing queue
class queue:
    def __init__(self):
        self.value=[]
    def enqueue(self,x):
        # append is used to add value in list at the last index or place
         self.value.append(x)
    def dequeue(self):
       front =self.value[0]
       self.value=self.value[1:]
       return front
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.value)
q.enqueue(40)
print(q.value)
print(q.dequeue())
# binary search:
#     hard code -- array
# array=[1,2,3,4,5]
# print(array)
#     input from user -- array
n=int(input("Enter the size of array:"))
array=[]
for i in range(n):
    array.append(int(input("Enter value of array:")))
print(array)
#   issue of pass by reference
# def sort(arr,x):
#     for i in range(x):
#         for j in range(x-1):
#             if(arr[j]>arr[i]):
#                 arr[i],arr[j]=arr[j],arr[i]
#     # print(arr)
# print(array)
# sort(array,n)
for i in range(n):
    for j in range(n-1):
        if(array[j]>array[i]):
            array[i],array[j]=array[j],array[i]
print(array)
y=int(input("Enter the number you want to search:"))
def binary(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
z=binary(array,y)
print("ypur index is:")
print(z)
        



   



