def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num =6
print_factors(num)
num=6
if(num):
    fact=1
    for i in range(1,int(num)+1):
        fact=fact*i
        num=6
        print("factorial is",fact)
else :
    print("error")
