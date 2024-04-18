marks1=int(input("Enter the marks in sub 1"))
marks2=int(input("Enter the marks in sub 2"))
marks3=int(input("Enter the marks in sub 3"))

average=((marks1+marks2+marks3)/3)
if(average>=90 and average<100):
    print("A")
elif(average>=80 and average<89):
    print("B")
elif(average>=70 and average<79):
    print("C")
elif(average>=60 and average<69):
    print("D")
else:
    print("F")
