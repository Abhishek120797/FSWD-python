def square_num(n):
    x=1
    while n:
        yield x**2
        x+=1
        n-=1
for e in square_num(int(input("Enter a number : "))):
    print(e,end=' ')
