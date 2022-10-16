class User:
    def __init__(self,name="dfault",age=0,email="abc@gamil.com"):
        self.name=name
        self.age=age
        self.email=email
    
    def getUser(self):
        print(self.name,self.age,self.email)

    def youngest(user1,user2,user3):
        if user1.age<user2.age and user1.age<user3.age:
            print(user1.name," is youngest")
        if user2.age<user1.age and user2.age<user3.age:
            print(user2.name," is youngest")
        if user3.age<user1.age and user3.age<user2.age:
            print(user3.name," is youngest")

user1=User("Abhishek",26,"abhi.jais1211@gmail.com")
user2=User("vicky",25,"vicky.jais1211@gmail.com")
user3=User("saransh",8,"saransh.jais1407@gmail.com")
User.youngest(user1,user2,user3)