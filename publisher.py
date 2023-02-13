class publisher:
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("Name:",self.pname)
class book(publisher):
    def __init__(self,pname,bname,author):
        self.pname=pname
        self.bname=bname
        self.author=author
    def display(self):
        print("pname:",self.pname)
        print("bname:",self.bname)
        print("author:",self.author)
class python(book):
    def __init__(self,pname,bname,author,page,price):
        self.pname=pname
        self.bname=bname
        self.author=author
        self.page=page
        self.price=price
    def display(self):
        print("Publisher Name:",self.pname)
        print("Book Name:",self.bname)
        print("Author:",self.author)
        print("Page:",self.page)
        print("Price:",self.price)
n=input("Enter Publisher:")
b=input("Enter Book Name:")
t=input("Enter Author Name:")
p=int(input("Enter Page No:"))
pr=int(input("Enter Price:"))
obj=python(n,b,t,p,pr)
obj.display()
