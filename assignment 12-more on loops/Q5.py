num=int(input("Enter a number : "))
r=range(num+1,num*10)
for x in r:
    z=range(2,x)
    for y in z:
        if x%y==0:
            break;
    else:
        print(x,end=" ")
        break;
