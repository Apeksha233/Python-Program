def unique(L):
    a=[]
    for b in L:
        if b not in a:
            a.append(b)
    return a
print(unique([10,2,3,1,2,3,11,4]))