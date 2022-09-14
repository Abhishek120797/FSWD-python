def checkprime(n):
    for e in range(2,n):
        if n%e==0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is prime number")
checkprime(int(input("Enter a number : ")))
