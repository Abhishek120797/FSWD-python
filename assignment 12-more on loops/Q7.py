num_1=int(input("Enter firs number : "))
num_2=int(input("Enter second number : "))
temp=0
count=0
temp=num_1 if num_1>num_2 else num_2
i=2
while i<=temp:
    if num_1%i==00 and num_2%i==0:
        count+=1
    i+=1
print("co-prime number") if count==0 else print("not a co-prime number")
