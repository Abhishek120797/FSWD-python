def sum_digit(n):
    if n//10==0:
        return n
    add=sum_digit(n//10)+n%10
    return add

num=int(input("Enter a number : "))
print("sum of digit  of number  {} is {}".format(num,sum_digit(num)))