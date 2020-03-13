list=[]
f=True
while f:
    print("Enter a number")
    a=int(input())
    if a<=1000: list.append(a)
    else: f=False
print("Sum is ", sum(list))
print("The average number is ", sum(list)/len(list))
print("The minimal number is ", min(list))
print("The maximal number is ", max(list))