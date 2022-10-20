g=input("enter the grade:")
s=int(input("enter the salary:"))
tot=0
if(s<0):
    print("invalid input")
else:
    if(g=='A' and s>10000):
        bonus=0.05*s
        tot=bonus+s
    elif(g=='B' and s>10000):
        bonus=0.1*s
        tot=bonus+s
    elif(g=='A' and s<10000):
        bonus=0.07*s
        tot=bonus+s
    elif(g=='B' and s<10000):
        bonus=0.12*s
        tot=bonus+s
    print(s)
    print(bonus)
    print("total amount is:",tot)

    
