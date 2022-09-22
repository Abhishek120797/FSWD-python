def prime_num(n):
    num=2
    while n:
        for e in range(2,num):
            if num%e==0:
                break
        else:
            yield num
            n-=1
        num+=1
for p in prime_num(int(input('Enter a number : '))):
    print(p,end=' ')
