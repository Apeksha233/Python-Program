n=int(input("Enter no:"))
n1=n
s=0
while n1>0:
    digit=n1%10
    s=s+digit**3
    n1//=10
if n==s:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

