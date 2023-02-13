def fileRead(fname):
    with open(fname,"r") as file:
        list1=file.readlines()
        print(list1)
fileRead("sample.txt")
