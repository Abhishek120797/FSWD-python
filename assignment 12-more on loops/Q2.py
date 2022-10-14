num=int(input("Enter a number : "))
r=range(2,num)
for e in r:
    if num%e==0:
        print(num," is not prime number")
        break;
else:
    print(num," is prime number")
