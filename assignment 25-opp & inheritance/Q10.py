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

class Phone:
    
    def calling(self):
        print('calling..')

    def sms(self):
        print('sms')

class Truecaller():
    contact={"abhishek":7758938495,"vicky":8830274339}

    @classmethod
    def fetch(cls,key):
        print(cls.contact[key])

    @classmethod
    def add_contact(cls,key,value):
        cls.contact[key]=value

    @classmethod
    def getContact(cls):
        print(cls.contact)

class Smartphone(Phone,Caluletor2,Truecaller):
    
    def smartfetch(self,key):
        self.fetch(key)

true=Truecaller()
true.fetch("abhishek")
user1=Smartphone()
user1.fetch("vicky")