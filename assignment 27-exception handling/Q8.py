def division():
    try:
        num_1=int(input("Enter dividend : "))
        num_2=int(input("Enter divisor : "))
        ans=num_1/num_2
    except ValueError:
        print("please enter only number")
        division()
    except ArithmeticError:
        print("diviser not sholud be Zero")
        division()
    else:
        print("{} is divided by {} and result is {}".format(num_1,num_2,ans))
division()
