r=range(2,101)
for x in r:
    z=range(2,x)
    for y in z:
        if x%y==0:
            break;
    else:
        print(x,end=" ")
