n = int(input("Enter the Range First :"))
f = False
if n<2:
    
    print("Not a prime Number if it is < 2")
else:
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            f = True
            break
if f :
    print("not a prime")
else:
    print("Prime")

    