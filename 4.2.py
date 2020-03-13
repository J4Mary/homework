import random
n=['Mary', 'Max', 'Lera', 'Alex', 'Anton']
f=['Grey', 'Black', "Green", 'McFly', 'Stone']
list=[]
for i in range(0,25):
    s=random.choice(n)+' '+random.choice(f)
    list.append(s)
for j in range(0,25):
    print(list[j],' - ', list.count(list[j]))