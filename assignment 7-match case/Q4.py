age=int(input("Enter your Age : "))
if age>=60:
    print("senior citizen")
elif age>=40 and age<60:
    print("Experienced")
elif age>=20 and age<40:
    print("Young")
elif age>=10 and age<20:
    print("teen")
else:
    print("kid")
