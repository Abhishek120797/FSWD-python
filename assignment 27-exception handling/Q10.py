def division():
    try:
        num_1=int(input("Enter dividend : "))
        try:
            num_2=int(input("Enter divisor : "))
        except ValueError:
            print("please enter only number")
            division()
        try:
            ans=num_1/num_2
            print("{} id divided by {} and result is {}".format(num_1,num_2,ans))
        except ZeroDivisionError:
            print("diviser not sholud be Zero")
            division()
    except ValueError:
            print("please enter only number")
            division()
    except Exception:
        print("some error occured")
division()
