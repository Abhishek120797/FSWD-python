a=int(input('Enter a first number = '))
b=int(input('Enter a second number = '))
c=int(input('Enter a third number = '))
if a>b and a>c:
    print(a,' is greater number ')
elif b>a and b>c:
    print(b,' is greater number')
elif c>a and c>b:
    print(c,' is greater number')
elif a==b and b==c:
    print(a)
elif a==b:
    print(a)
elif b==c:
    print(b)
elif a==c:
    print(c)
