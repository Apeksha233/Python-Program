s=input("Enter String:")
w=s.split()
for s1 in w:
    for i in range(len(s1)-1,-1,-1):
        print(s1[i],end=" ")
        print("",end=" ")
