def perfect(n):
    ret=[]
    for i in range(2,n):
        ilist=[]
        for j in range(2,int(i/2)):
            if i%j==0 and j<i/j:
                ilist.append(j)
                ilist.append(i/j)
        if sum(ilist)+1==i:
            ret.append(i)
    return ret

a=perfect(10000)
print(a)