def print_Square(n):
    if n>=1:
        print_Square(n-1)
        print(n**2,end=" ")
       
num_1=int(input("Enter a number : "))
print_Square(num_1)
