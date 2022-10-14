def fabonacci(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for e in fabonacci(int(input("Enter a number : "))):
    print(e,end=' ')
