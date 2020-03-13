students=dict([('Mary',[9,9,10,9]),('Alex',[10,10,9,10]),('Max',[9,8,10,8]),('Lera',[10,9,10,9])])
print(students)
for key,val in students.items():
    students[key]=sum(val)/len(val)
print(students)
for key,val in students.items():
    if val==max(students.values()):
        print(key, 'is the best')
    if val==min(students.values()):
        print(key, 'is a loser')