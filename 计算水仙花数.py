alist=[]
for i in range(100,1000):
    a=i%10
    b=(i%100-a)/10
    c=(i-b*10-a)/100
    if a*a*a+b*b*b+c*c*c==i:
        alist.append(i)

print(alist)