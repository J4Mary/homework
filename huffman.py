#я пыталась, но у меня ничего не вышло :(
#функция считает кол-во символом в тексте
def count_char(text,char):
    count=0
    for c in text:
        if c==char:
            count +=1
    return count
f=open('a.txt', 'r')
g=open('b.txt', 'w')
#записывает весь текст из документа а в строку
s = ""
for line in f:
    s+=line
#создаем список, который в моем с++ воображении должен быть структурой(символ,вероятность,кодировка)
d={}
i=0 #должно как-то меняться, но я хз как
for char in "abcdefghijklmnopqrstuvwxyz .,?!-\n":
    d=dict(char, 100*count_char(s,char)/len(s))#записываем в первую ячейку символ
#сортировка list по убыванию вероятностей
for i in range(0, len(list)-1):
    for j in range(0,len(list)-1-i):
        if list[j][1]>list[j+1][1]:
            list[j][1], list[j + 1][1]=list[j + 1][1],list[j][1]
        j+=1
    i+=1
derevo=list#derevo нужно, чтоб без зазрения совести удалять из него элементы
imin1=imin2=0
p=0
while p<=1:
    #ищем индексы двух минимальных элементов
    for i in range(0,len(derevo)):
        if derevo[imin1]>derevo[i][1]:
            imin1=i
    for i in range(0, len(derevo)):
        if derevo[imin2] > derevo[i][1] and imin2!=imin1:
            imin2 = i
    #присваиваем верхнему "1", нижнему "0"(в list, кодировка) и объединяем их в один в derevo
    if imin1<imin2:
        list[imin2][2]+='0'
        list[imin1][2] += '1'
        derevo[imin1][1]=p=derevo[imin1][1]+derevo[imin2][1]
        del(derevo[imin2])
    else:
        list[imin2][2] += '1'
        list[imin1][2] += '0'
        derevo[imin2][1] = p = derevo[imin1][1] + derevo[imin2][1]
        del (derevo[imin1])
#на этом моменте я заметила ошибку при формировании list и теперь хз, что с этим дальше делать
#здесь еще нужно реверзнуть кодировку в list
#и записать все в новый документ
g.write("\n")
f.close()
g.close()