num1=int(input("Enter a first number : "))
num2=int(input("Enter a second number : "))
i=2
flag=0
while flag==0:
    if i%num1==0 and i%num2==0:
        print(i)
        flag=1
        break;
    i+=1
