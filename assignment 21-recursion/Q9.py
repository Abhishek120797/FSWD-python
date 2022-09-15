def print_multi(n,multi):
    if n>=1:
        print_multi(n-1,multi)
        print(n*multi,end=" ")
       
num_1=int(input("Enter a number multiples : "))
num_2=int(input("Enter a number : "))
print_multi(num_1,num_2)
