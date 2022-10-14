a=int(input('Enter a year number = ')) 
if a%400==0 or a%100!=0 and a%4==0:
    print(a,' is leap year')
else:
    print(a,' is not leap year')
