def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n

num=int(input("Enter a number : "))
print("factorial of {} is {}".format(num,fact(num)))