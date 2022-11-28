import datetime
today=datetime.date.today()
currentyear=today.year
print(currentyear)
print("enter lastyear")
endyear(int(input())
    print("list of leapyear:")
        for year in range(currentyear,endyear):
        if(0==year%4)and(0!=year%100)or(0==year%400):
        print(year)
        
