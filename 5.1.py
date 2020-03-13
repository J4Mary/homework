def down(str):
    return str.lower()
def up(str):
    return str.upper()
str=["Father", "Mother", "SISTER", "brother"]
s1=list(map(down,str))
print(s1)
s2=list(map(up,str))
print(s2)