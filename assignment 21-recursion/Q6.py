def print_even(n):
    if n>=1:
        print(n*2,end=" ")
        print_even(n-1)
       
num_1=int(input("Enter a number : "))
print_even(num_1)