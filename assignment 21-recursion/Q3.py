def print_odd(n):
    if n>=1:
        print_odd(n-1)
        print(n*2-1,end=" ")
       
num_1=int(input("Enter a number : "))
print_odd(num_1)