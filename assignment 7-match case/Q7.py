num=int(input("Enter any number: "))
match num>0:
    case 1:
        print("number is positive")
    case 0:
        match num<0:
            case 1:
                print("number is negative")
            case 0:
                print("number is zero")
