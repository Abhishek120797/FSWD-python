def print_reverse(n):
    if n>=1:
        print(n%10,end="")
        print_reverse(n//10)
       
num_1=int(input("Enter a number : "))
print_reverse(num_1)