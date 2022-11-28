list=[]
n=int(input("enter the number of colors:"))
for i in range(0,n):
    list.append(str(input()))
print(list)
print("the first color is:",list[0])
print("the last color is:",list[-1])
