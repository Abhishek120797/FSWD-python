def octal(n):
    if n>7:
        octal(n//8)
    print(n%8,end="")

num=int(input("Enter a number : "))
octal(num)