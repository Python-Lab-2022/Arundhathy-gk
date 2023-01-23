
class rectangle:
        def __init__(self,breadth,length):
           self.breadth1=breadth
           self.length1=length
        def area(self):
           return self.breadth1*self.length1
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
obj=rectangle(length,breadth)
print("area of rectagle:",obj.area())
