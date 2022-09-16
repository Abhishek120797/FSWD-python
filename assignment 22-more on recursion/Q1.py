def sum_N(n):
    if n==1:
        return 1
    return sum_N(n-1)+n

num=int(input("Enter a number : "))
print("sum of first {} natural number is {}".format(num,sum_N(num)))
