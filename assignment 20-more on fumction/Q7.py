def calculate(a,b):
    print("sum of {} and {} is {}".format(a,b,add(a,b)))

def add(x,y):
    return x+y
        
num_1=int(input("Enter first number : "))
num_2=int(input("Enter secon number : "))
calculate(num_1,num_2)
