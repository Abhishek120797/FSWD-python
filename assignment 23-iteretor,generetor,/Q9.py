def decor_trangle(perimeter_func):
    def check_trangle(l1,l2,l3):
        if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
            print("trangle exist with this side")
            return perimeter_func(l1,l2,l3)
        else:
            print("trangle not exist with this side")
    return check_trangle

@decor_trangle
def perimeter(l1,l2,l3):
    print("perimeter of trangle is {}".format(l1+l2+l3))

side_1=float(input("Enter first side of trangle : "))
side_2=float(input("Enter second side of trangle : "))
side_3=float(input("Enter third side of trangle : "))
perimeter(side_1,side_2,side_3)



