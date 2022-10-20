p=int(input("enter the marks in python:"))
c=int(input("enter the marks in c:"))
m=int(input("enter the marks in mathematics:"))
phy=int(input("enter the marks in pysics:"))
total=p+c+m+phy
aggregate=total/4
print("total",total)
print("aggregate",aggregate)
if(aggregate>75):
    print("distinction")
elif(aggregate>=60 and aggregate<75):
    print("first distinction")
elif(aggregate>=50 and aggregate<60):
    print("second distinction")
elif(aggregate>=40 and aggregate<50):
    print("third distinction")
else:
    print("fail")
    
        
