def print_even(n):
    if n>=1:
        print_even(n-1)
        print(n*2,end=" ")
       
num_1=int(input("Enter a number : "))
print_even(num_1)