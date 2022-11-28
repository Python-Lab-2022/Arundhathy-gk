list=[]
n=int(input("enter the numbers:"))
for i in range(0,n):
    list.append(int(input()))
print(list)
for i in list:
    if i >100:
        print("greaterthan 100 numbers are:")
        print(i)
print("over")
    
