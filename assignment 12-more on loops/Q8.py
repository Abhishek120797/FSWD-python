num=int(input("Enter first number : "))
a1=-1
a2=1
i=0
while i<num:
    fab=a1+a2
    print(fab,end=" ")
    a1=a2
    a2=fab
    i+=1
