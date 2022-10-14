def nthfeb(n):
    if n==0 or n==1:
        return n
    return nthfeb(n-1)+nthfeb(n-2)

nth=int(input("Enter a number : "))
print("{}th term of febonacci series is {}".format(nth,nthfeb(nth)))