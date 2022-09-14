while(1):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.division")
    print("5.Exit")
    x=int(input("Enter your choice beetween 1 to 5 ="))
    match x:
        case 1:
            a=float(input("Enter first number : "))
            b=float(input("Enter second number : "))
            c=a+b
            print("sum of ",a," and ",b," is ",c)
            print()
        case 2:
            a=float(input("Enter first number : "))
            b=float(input("Enter second number : "))
            c=a-b
            print("diffirence of ",a," and ",b," is ",c)
            print()
        case 3:
            a=float(input("Enter first number : "))
            b=float(input("Enter second number : "))
            c=a*b
            print("product of ",a," and ",b," is ",c)
            print()
        case 4:
            a=float(input("Enter dividend : "))
            b=float(input("Enter diviser : "))
            c=a/b
            print(a,"/",b,"=",c)
            print()
        case 5:
            if x==5:
                break;
        case _:
            print("Invalid choice")
	        