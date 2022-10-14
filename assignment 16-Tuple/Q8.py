tuple1 =(('a', 21),('b', 37),('c', 11), ('d',29))
print("original tuple {}".format(tuple1))
tuple1=list(tuple1)
for i in range(4):
    for j in range(4):
        if tuple1[i][1]<tuple1[j][1]:
           temp=tuple1[i]
           tuple1[i]=tuple1[j]
           tuple1[j]=temp
tuple1=tuple(tuple1)
print("sorted tuple {}".format(tuple1))
