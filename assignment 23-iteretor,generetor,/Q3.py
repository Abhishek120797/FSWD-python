def even_num(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1
for e in even_num(int(input("Enter a number : "))):
    print(e,end=' ')
