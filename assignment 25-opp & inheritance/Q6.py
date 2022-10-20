class Calculetor:
    def add(self,num1,num2):
        return num1+num2
    
    def sub(delf,num1,num2):
        return num1-num2

class Caluletor2(Calculetor):

    def multi(self,num1,num2):
        return num1*num2
    
    def division(self,num1,num2):
        return num1/num2

user1=Caluletor2()
print(user1.add(10,20))
print(user1.sub(20,10))
print(user1.multi(10,20))
print(user1.division(20,10))