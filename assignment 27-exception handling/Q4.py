def divide():
    try:
        a=int(input("Enter a dividend : "))
        b=int(input("Enter a divisor : "))
        print("{} divide by {} ={}".format(a,b,a/b))
    except ValueError:
        print("please Enter number only")
        divide()
divide()
