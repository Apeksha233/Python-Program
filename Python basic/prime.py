n=int(input("Enter no:"))
s=0
for i in range(2,n):
    if(n%i==0):
        s=1
        break
if s==0:
    print("Number is prime")
else:
    print("Number is not prime")
