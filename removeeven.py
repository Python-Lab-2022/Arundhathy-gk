list = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    evenList.append(listValue)

print("List Items = ", evenList)

evenList = [ev for ev in evenList if ev % 2 != 0]    
print("List Items after removing even Items = ", evenList)
