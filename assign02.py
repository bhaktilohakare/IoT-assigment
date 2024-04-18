n=int(input("Enter the Number :"))
a=int(n%10)
n=n/10
b=int(n%10)
n=n/10
c=int(n%10)
n=n/10
d=int(n%10)

print(f"{d} {c} {b} {a} ")
print(f"9361={d*1000}+{c*100}+{b*10}+{a} ")
print(f"{a}{b}{c}{d}")


