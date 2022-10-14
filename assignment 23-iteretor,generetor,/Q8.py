def prime_num():
    n=2
    while True:
        for e in range(2,n):
            if n%e==0:
                break
        else:
            yield n
        n+=1
num=prime_num()
while True:    
    ans=input("do you want to generate another prime number[y/n] : " )
    if ans=='y':
        print(next(num))
    else:
        break
