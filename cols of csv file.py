import csv
with open("excel.csv",newline="")as csvfile1:
    data=csv.DictReader(csvfile1)
    print("roll no name")
    print("-------------")
    for row in data:
        print(row['roll no'],row['name'])
