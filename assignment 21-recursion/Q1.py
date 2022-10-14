def printN(n):
    if n>=1:
        printN(n-1)
        print(n,end=" ")

num_1=int(input("Enter a number : "))
printN(num_1)
