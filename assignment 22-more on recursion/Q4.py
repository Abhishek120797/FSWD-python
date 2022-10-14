def sum_square(n):
    if n==1:
        return 1
    return sum_square(n-1)+n**2

num=int(input("Enter a number : "))
print("sum of square first {} natural number is {}".format(num,sum_square(num)))