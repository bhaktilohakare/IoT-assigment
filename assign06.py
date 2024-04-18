def fact(n):
    facta=1
    if n==0 or n==1:
        return 1
    else:
        return (n*fact(n-1))
    
n=int(input("Enter the number"))
f=fact(n)
print(f)        