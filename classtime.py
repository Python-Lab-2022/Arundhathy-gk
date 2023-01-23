class time:
    def __init__(self,h,m,s):
        self.hr=h
        self.min=m
        self.sec=s
    def __add__(self,other):
        tempsec=self.sec+other.sec
        tempmin=tempsec/60
        self.sec=int(tempsec%60)
        self.min=self.min+other.min+tempmin
        temphr=self.min/60
        self.min=int(self.min%60)
        self.hr=int(self.hr+other.hr+temphr)
        return time(self.hr,self.min,self.sec)
    def __str__(self):
        return str(self.hr)+'hr '+str(self.min)+'min '+str(self.sec)+'sec'
t1=time(5,60,4)
t2=time(2,4,4)
print(t1+t2)
