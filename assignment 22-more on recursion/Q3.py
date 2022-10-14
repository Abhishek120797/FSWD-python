def sum_even(n):
    if n==1:
        return 1
    return sum_even(n-1)+n*2

num=int(input("Enter a number : "))
print("sum of first {} even natural number is {}".format(num,sum_even(num)))