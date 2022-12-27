a=float(input("enter the side:"))
s_area=lambda a:a*a
print("Area of Square=",s_area(a))

l=float(input("Enter the Length:"))
w=float(input("Enter the Width:"))
r_area=lambda l,w:l*w
print("Area of Rectangle=",r_area(l,w))

b=float(input("Enter the Base:"))
h=float(input("Enter the Height:"))
t_area=lambda b,h:(h*b)/2
print("Area of Triangle=",t_area(b,h))
      
