def decor_prime(find_hcf_func):
    def co_prime(num_1,num_2):
        temp=0
        count=0
        temp=num_1 if num_1>num_2 else num_2
        i=2
        while i<=temp:
            if num_1%i==00 and num_2%i==0:
                count+=1
            i+=1
        if count==0:
            print("co-prime number")
        else:
            print("not a co-prime number")
        return find_hcf_func(num_1,num_2)
    return co_prime
    
@decor_prime
def find_hcf(num_1,num_2):
    if num1>num2:
        i=num1
    else:
        i=num2
    flag=0
    while flag==0:
        if num1%i==0 and num2%i==0:
            print("hcf of {} and {} is {}".format(num_1,num_2,i))
            flag=1
            break
        i-=1
    
num1=int(input("Enter first number : "))
num2=int(input("Emter second number : "))
find_hcf(num1,num2)
