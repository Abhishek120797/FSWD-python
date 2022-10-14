num=int(input('Enter a number = '))
count=0
while num!=0:
    num=num//10
    count=count+1
if count==3:
    print('given number is three digit number')
else:
    print('given number is not a three digit number')
