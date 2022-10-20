n=input("enter the number:")
if(n.isnumeric()):
    fact=1
    for i in range(1,int(n)+1):
        fact=fact*i
        print("factorial is",fact)
else:
    print("enter the number")
