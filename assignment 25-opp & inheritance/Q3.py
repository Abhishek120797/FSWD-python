class Profile:
    def __init__(self,name,email,age):
        self.name=name
        self.__email=email
        self.__age=age

    def getuser(self):
        print(self.name,self.__email,self.__age)

    def UpdateName(self,name):
        self.name=name

    def UpdateEmail(self,email):
        self.__email=email

    def UpdateAge(self,age):
        self.__age=age

user1=Profile("abhishek","abhi.jais1211@gmail.com",26)
user1.getuser()
user1.name="vicky"
user1.__email="vicky.jais1211@gmail.com"
user1.__age=27
print("email and age not updated")
user1.getuser()