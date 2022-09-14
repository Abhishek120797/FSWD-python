r=range(int(input("Enter first number : ")),int(input("Enter second number : ")))
for x in r:
    z=range(2,x)
    for y in z:
        if x%y==0:
            break;
    else:
        print(x,end=" ")
