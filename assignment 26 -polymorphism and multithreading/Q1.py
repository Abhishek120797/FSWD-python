from time import clock_settime


class Calculetor:

    def multiply(self,num1,num2,num3=1,num4=1):
        return num1*num2*num3*num4

user1=Calculetor()
print(user1.multiply(5,6))
print(user1.multiply(5,6,7))
print(user1.multiply(5,6,7,8))