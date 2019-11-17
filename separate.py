
list=[1,2,4.5,"Barsha",6,7.1,"Rusha"]
listint=[]
liststr=[]
listfloat=[]
for x in list:
    if type(x)==int:
        listint.append(x)
    elif type(x)==str:
        liststr.append(x)
    else:
        listfloat.append(x)
print(list)
print(listint)
print(liststr)
print(listfloat)