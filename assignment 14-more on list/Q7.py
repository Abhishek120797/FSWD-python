Nlist=[1,2,3,'A',4,True,34.5,5,2+3j,6]
intlist=[]
for e in Nlist:
    if type(e)==int:
        intlist.append(e)
Nlist=intlist
print(Nlist)
