import csv
with open("excel1.csv",newline="")as csvfile1:
    data=csv.DictReader(csvfile1)
    print("ROLL NO NAME")
    print("-------------")
    for row in data:
        print(row['ROLL NO'],row['NAME'])
