num1=int(input("Enter a first number : "))
num2=int(input("Enter a second number : "))
if num1>num2:
    i=num1
else:
    i=num2
flag=0
while flag==0:
    if num1%i==0 and num2%i==0:
        print(i)
        flag=1
