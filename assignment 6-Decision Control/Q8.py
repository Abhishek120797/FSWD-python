a=int(input('Enter coificient of quadratic term'))
b=int(input('Enter coificient of liner term'))
c=int(input('Enter constatnt term'))
disc=(b**2)-(4*a*c)
if disc>0:
    print('roots are real and distinct')
elif disc==0:
    print('roots are real and Equal')
elif disc<0:
    print('imaginary roots')
