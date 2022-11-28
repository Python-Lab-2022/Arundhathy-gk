list1=[1,5,6,8,9]
list2=[3,5,45,74,34]
print(len(list1))
print(len(list2))
if len(list1)==len(list2):
    print("list are same length")
else:
    print("different length")
x=sum(list1)
print(x)
y=sum(list2)
print(y)
if x==y:
     print("same")
else:
    print("not same")
num=int(input("enter a number"))
if num in list1 and list2:
    print (num)
else:
    print("element not in list")
common=set(list1).intersection(list2)
print(common,"occur in both")

