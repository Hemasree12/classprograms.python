a=int(input("enter the no.of fresh loves purchased:"))
b=int(input("enter the no.of old loves purchased:"))
c=a*185
d=b*(185*(60/100))
if(a<0 and b<0):
     print("Invalid input")
else:
    print("amount of new loaves",c) 
    print("amount of old loaves",d)
    print("total amount",c+d)
    
