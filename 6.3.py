Python={'Mary','Alex','Bill','Nick','Greg'}
FrontEnd={'Mary','Garry','Max','Nick'}
FullStack={'Mary','Dan','Ann','Bill'}
Java={'Mary','Dan','Alex','Molly'}
s={}
s=Python|FrontEnd|FullStack|Java
l=list(Python)+list(FullStack)+list(FrontEnd)+list(Java)
super=[]
for name in s:
    if l.count(name)>1:
        super.append(name)
print(super, 'are in several classes')
nF=s-FrontEnd
print(nF, 'are not in FrontEnd')
PorJ=Python|Java
print(PorJ, 'are studying Python or Java')