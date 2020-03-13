f=open('text.txt', 'r')
l1=[line.split() for line in f]
print(l1)
l2=[el for line in l1 for el in line]
print(l2)
l3=[l2.count(el) for el in l2]
print(l3)
l4=list(zip(l2,l3))
print(l4)
f.close()