limit=int(input("enter the limit:"))
r=0
m=2
while(r<limit):
    for n in range(1,m+1):
        p=m*m-n*n
        q=2*m*n
        r=m*m+n*n
        if(r>limit):
            break
        if(p==0 or q==0 or r==0):
            break
        print(p,q,r)
        m=m+1
