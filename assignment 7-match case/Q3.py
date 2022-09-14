while(1):
    print("a.check isosceles trangle")
    print("b.check right angled trangle")
    print("c.check equiletral trangle")
    print("d.Exit")
    choice=str(input("Enter your choice among a,b,c,d : "))
    match choice:
        case 'a':
            x=float(input("Enter length of sides first :"))
            y=float(input("Enter length of sides second :"))
            z=float(input("Enter length of sides third :"))
            if x==y!=z:
                print("given sides are of isosceles trangle")
            elif x==z!=y:
                print("given sides are of isosceles trangle")
            elif y==z!=x:
                print("given sides are of isosceles trangle")
            else:
                print("given sides are not of isosceles trangle")
                    
            print()
        case 'b':
            x=float(input("Enter length of  height :"))
            y=float(input("Enter length of  base :"))
            z=float(input("Enter length of  hypotenious :"))
            if x**2+y**2==z**2:
                print("given sides are of right angled trangle")
            else:
                print("given sides are not of right angled trangle")
            print()
        case 'c':
            x=float(input("Enter length of sides first :"))
            y=float(input("Enter length of sides second :"))
            z=float(input("Enter length of sides third :"))
            if x==y==z:
                print("given sides are of equilateral trangle")
            else:
                print("given sides are not of equlateral trangle")
            print()
        case 'd':
            if choice=='d':
                break;
        case _:
            print("Invalid choice")
            print()
