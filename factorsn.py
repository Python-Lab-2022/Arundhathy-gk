def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
    return
n=int(input("Enter a number:"))
print("All factors of",n,"are")
factors(n)
