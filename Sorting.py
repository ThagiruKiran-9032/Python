#PRIME NUMBERS
# 1. number less than 2 not a prime
# 2. numbers above 2 which are divisible by itself is calledd prime
# 3. no factors are allowed

n = int(input())
for i in range(2,n+1):
    if n % 2 ==0:
        print("Not a prime")
    else:
        print("Prime")