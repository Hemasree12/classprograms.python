a=int(input("Enter the value of a "))
b=int(input("enter the value of b"))
for i in range (a+1,b+1):
    com=0
    for j in range(1,b+1):
        if(i%j==0):
            com=com+1
    if(com>2):
        print(i,end=" ")
