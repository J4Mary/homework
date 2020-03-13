size={'XXS':{'Russia':42,'Germany':36,'USA':8,'France':38,'Great Britain':24, 'hip girth': range(89,92), 'the waist':range(63,65)},
      'XS':{'Russia':44,'Germany':38,'USA':10,'France':40,'Great Britain':26, 'hip girth': range(93,96), 'the waist':range(66,69)},
      'S':{'Russia':46,'Germany':40,'USA':12,'France':42,'Great Britain':28, 'hip girth': range(97,101), 'the waist':range(70,74)},
      'M':{'Russia':48,'Germany':42,'USA':14,'France':44,'Great Britain':30, 'hip girth': range(102,104), 'the waist':range(75,78)},
      'L':{'Russia':50,'Germany':44,'USA':16,'France':46,'Great Britain':32, 'hip girth': range(105,108), 'the waist':range(79,83)},
      'XL':{'Russia':52,'Germany':46,'USA':18,'France':48,'Great Britain':34, 'hip girth': range(109,112), 'the waist':range(84,89)},
      'XXL':{'Russia':54,'Germany':48,'USA':20,'France':50,'Great Britain':36, 'hip girth': range(113,117), 'the waist':range(90,94)},
      'XXXL':{'Russia':56,'Germany':50,'USA':22,'France':52,'Great Britain':38, 'hip girth': range(118,122), 'the waist':range(95,97)}}
def s(have,want):
    print(size[have][want])
print("Enter a size you have")
have=input()
print("Enter what you want")
want=input()
s(have,want)