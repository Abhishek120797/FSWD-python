class Profile:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
    def getuser(self):
        print(self.name,self.email,self.age)

user1=Profile("abhishek","abhi.jais1211@gmail.com",26)
user1.getuser()