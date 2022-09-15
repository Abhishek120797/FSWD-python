def printN(n):
    if n>=1:
        print(n,end=" ")
        printN(n-1)
       
num_1=int(input("Enter a number : "))
printN(num_1)
