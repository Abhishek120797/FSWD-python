def addition(num_1,num_2):
    print("Addition of {} and {} is {}".format(num_1,num_2,num_1+num_2))

def subtraction(num_1,num_2):
    print("subtraction of {} and {} is {}".format(num_1,num_2,num_1-num_2))

def multiplication(num_1,num_2):
    print("Multiplication of {} and {} is {}".format(num_1,num_2,num_1*num_2))

def division():
    try:
        num_1=input_num_1()
        num_2=input_num_2()
        print("{} divid by {} is eqal to {}".format(num_1,num_2,num_1/num_2))
    except ArithmeticError:
        print("divisor not should Zero")
        division()
def input_num_1():
    try:
        return int(input("Enter first number : "))
    except ValueError:
        print("Error :please Enter only numbers")
        input_num_1()
def input_num_2():
    try:
        return int(input("Enter second number :"))
    except ValueError:
        print("Error :Enter only numbers")
        input_num_2()


def calculetor():
    print()
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    print()
    choice=int(input("Enter your choice between(1 to 5) :"))
    print()
    match choice:
        case 1:
            N_1=input_num_1()
            N_2=input_num_2()
            addition(N_1,N_2)
            calculetor()
        case 2:
            N_1=input_num_1()
            N_2=input_num_2()
            subtraction(N_1,N_2)
            calculetor()
        case 3:
            N_1=input_num_1()
            N_2=input_num_2()
            multiplication(N_1,N_2)
            calculetor()
        case 4:
            division()  
            calculetor()
        case 5:
            pass
        case _:
            print("please enter correct choice : ")
            calculetor()
calculetor()
