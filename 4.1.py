s1="Ukrain, Greece, Hungary"
s2="Welcome to California"
l1=s1.split(', ')
for country in l1:
    print(s2[:s2.find("California")]+country)