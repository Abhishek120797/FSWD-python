def sum_qube(n):
    if n==1:
        return 1
    return sum_qube(n-1)+n**3

num=int(input("Enter a number : "))
print("sum of qube first {} natural number is {}".format(num,sum_qube(num)))