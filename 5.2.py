def my_square(num):
    return num ** 2
l=[2,5,7,3,8,9,44,55]
numbers=[]
f=True
for el in l:
   for i in range(2, el):
      if el % i == 0:
          f = False
   if f==True: numbers.append(el)
print(numbers)
squared_numbers = list(map(my_square, numbers))
print(squared_numbers)