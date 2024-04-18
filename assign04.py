num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
num3=int(input("Enter num3"))
if(num1==num2==num3):
    print("all are equal")
elif(num1==num2 or num1==num3 or num3==num2):
    if(num1==num2 and num1>num3):
        print("num1 and num2 are equal and num3 is less than both")
    elif(num1==num2 and num1<num3):
        print("num1 and num2 are equal and num3 is greater than both")
    elif(num1==num3 and num1>num2):
        print("num1 and num3 are equal and num2 is less than both")
    elif(num1==num3 and num1<num2):
        print("num1 and num3 are equal and num2 is greater than both")
    elif(num3==num2 and num1<num3):
        print("num3 and num2 are equal and num1 is less than both")
    elif(num3==num2 and num1>num3):
        print("num3 and num2 are equal and num1 is greater than both")
elif(num1>num2 and num1>num3):
    print("num1 is greater ")
elif(num2>num3 and num2>num1):
    print("num2 is greater")
else:
    print("num3 is greater" )
    












"""
if(num1>=num2 ):
    if(num1==num2 and num1==num3):
        print("all are equal")
    elif(num1>num3):
        print("num1 is greater")
    else:
        print("num3 is greater")
elif(num2>=num1):
    if(num2>num3):
        print("num2 is greater")
    elif(num2==num1):
        print("num2 and num are equal")
    else:
        print("num3 is greater")
elif(num3>num2 and num3>num1):
    print("num3 is greater ")
else:
    print("all there are equal")
"""