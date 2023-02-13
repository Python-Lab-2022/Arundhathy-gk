import csv
with open("excel1.csv","r")as file:
    reader1=csv.reader(file)
    for row in reader1:
        print(row)
