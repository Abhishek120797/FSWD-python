def divide():
    try:
        a=int(input("Enter a dividend : "))
        b=int(input("Enter a divisor : "))
        print("{} divide by {} ={}".format(a,b,a/b))
    except ArithmeticError:
        print("divisor not should be Zero")
        divide()
divide()
