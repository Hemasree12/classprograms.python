import array as arr
a=arr.array('d',[1,2,4,5,5,5,6,6,7,2,0])
total=sum(a)
nlen=len(a)
mean=total/nlen
print("Mean is:",mean)
if nlen%2==0:
 median1=a[nlen//2]
 median2=a[nlen//-1]
 median=(median1+median2) /2
else:
 median=a[nlen//2]
print("Median is :"+str(median))
mode=a[0]
c=0
l=0
for i in range (len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
    else:
        if(c>l):
            mode=a[i]
            l=c
            c=0
            print("Mode is :", mode)
