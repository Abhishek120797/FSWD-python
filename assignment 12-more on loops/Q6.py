n=int(input("Enter a number : "))
count=0
i=2
while count<=n:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    else:
        print(i,end=" ")
        count+=1
    i+=1
