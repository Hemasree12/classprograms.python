age=int(input("enter the age:"))
if(age<0):
    print("invalid input")
elif(age>=18):
    printf("eligible")
else:
    print("not eligible")
    r=18-age
    print("u are allowed to vote after r years",r)
