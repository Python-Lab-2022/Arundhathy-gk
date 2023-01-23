class area:
    def __init__(self,m1,m2):
        self.l=m1
        self.b=m2
    def __gt__(self,other):
        r1=self.l*self.b
        r2=other.l*other.b
        if(r1>r2):
          return 1
        else:
          return 0
s1=area(1,5)
s2=area(2,6)
if(s1>s2):
    print("area of rect1 is greater")
else:
    print("area of rect2 is greater")
        
