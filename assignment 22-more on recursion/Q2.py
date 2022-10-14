def sum_odd(n):
    if n==1:
        return 1
    return sum_odd(n-1)+n*2-1

num=int(input("Enter a number : "))
print("sum of first {} odd natural number is {}".format(num,sum_odd(num)))