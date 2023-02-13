import csv
with open("excel.csv","r")as file:
    reader1=csv.reader(file)
    for row in reader1:
        print(row)
