a=int(input())
f=True
for i in range(2, a-1):
    if a%i==0:
        f=False
if f==True: print("The number is prime")
else: print("The number is not prime")