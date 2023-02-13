import math
def isPerfectSquare(i):
       if(i>=0):
              sr=int(math.sqrt(i))
              return ((sr*sr) == i)
       return false
list1=[]
list2=[]
l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
for i in range(l,u):
       list1.append(i)
for i in list1:
       if (isPerfectSquare(i)):
              list2.append(i)
print(list2)
             
