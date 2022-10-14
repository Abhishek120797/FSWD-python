a=int(input('Enter a month number = '))
match a:
    case 1:
        print('31 Days')
    case 2:
        print('28 Days')
    case 3:
        print('31 Days')
    case 4:
        print('30 Days')
    case 5:
        print('31 Days')
    case 6:
        print('30 Days')
    case 7:
        print('31 Days')
    case 8:
        print('31 Days')
    case 9:
        print('30 Days')
    case 10:
        print('31 Days')	
    case 11:
        print('30 Days')
    case 12:
        print('31 Days')
    case _:
        print('invalid month number')
