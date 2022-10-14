year=int(input("Enter a year : "))
if year%100==0:
    if year%4==0:
        print("Century leap year")
    else:
        print("Century non leap year")
else:
    if year%4==0:
        print("Non century leap year")
    else:
        print("Non century non leap year")
