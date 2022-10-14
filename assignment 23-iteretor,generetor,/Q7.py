def fabonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
term=fabonacci()
while True:    
    ans=input("do you want to generate another element[y/n] : " )
    if ans=='y':
        print(next(term))
    else:
        break
