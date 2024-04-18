def fact(n):
    facta=1
    for num in range(1,n+1):
        facta=num*facta
    print(facta)
n=int(input("Enter the number"))
for num in range(1,n+1):
    fact(num)
        
