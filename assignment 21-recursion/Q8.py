def print_Qube(n):
    if n>=1:
        print_Qube(n-1)
        print(n**3,end=" ")
       
num_1=int(input("Enter a number : "))
print_Qube(num_1)