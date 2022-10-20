class Profile:
    platform="student"
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def getuser(self):
        print(self.name,self.email,self.age)

    def UpdateName(self,name):
        self.name=name

    def UpdateEmail(self,email):
        self.email=email

    def UpdateAge(self,age):
        self.age=age

    @classmethod
    def getPlatform(cls):
        print(cls.platform)

    @classmethod
    def setPlatform(cls,platform):
        cls.platform=platform

user1=Profile("abhishek","abhi.jais1211@gmail.com",26)
user1.getuser()
user1.UpdateName("Vicky")
user1.UpdateEmail("vicky.jais1211@gmail.com")
user1.UpdateAge(27)
print("updated user details")
user1.getuser()
user1.getPlatform()
print("updated class variable")
Profile.setPlatform("Admin")
Profile.getPlatform()
