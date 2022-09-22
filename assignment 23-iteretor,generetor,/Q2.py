def odd_num(n):
    x=1
    while n:
        yield x
        x+=2
        n-=1
for e in odd_num(int(input("Enter a number : "))):
    print(e,end=' ')
