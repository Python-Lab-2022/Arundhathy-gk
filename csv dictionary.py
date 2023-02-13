import csv
csv_col=['id','name','place']
Dict_data=[{'id':1,'name':'anju','place':'kollam'},{'id':2,'name':'anu','place':'ekm'},{'id':3,'name':'kunju','place':'kannur'},{'id':4,'name':'ammu','place':'kannur'},{'id':5,'name':'anuji','place':'muv'}]
csv_file="names.csv"
try:
    with open(csv_file,'w')as file1:
        writer=csv.DictWriter(file1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in Dict_data:
         writer.writerow(data1)
except IOError:
    print("ioerror")
data1=csv.DictReader(open(csv_file))
print("csv file as dictionary:\n")
for row in data1:
    print(row)
