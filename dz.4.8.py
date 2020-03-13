list=[]
for i in range(1,11):
    print("Enter a number")
    list.append(int(input()))
l2=[x*2 for x in list]
print(l2)