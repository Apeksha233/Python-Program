s=input("Enter String:")
n=len(s)
f=0
if n%2==0:
    i=0
    j=n//2
    while i<n//2 and j<n:
        if s[i]==s[i]:
            i=i+1
            j=j+1
        else:
            f=1
            break
else:
    f=1
    if f==0:
        print("Symmetrical")
    else:
        print("Not Symmetrical")
f=0
i=0
j=n-1
while i<n:
    if s[i]==s[j]:
        i=i+1
        j=j-1
    else:
        f=1
        break
if f==0:
    print("Palindrom")
else:
    print("Not Palindrom")                            