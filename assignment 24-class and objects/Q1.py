class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    
    def getUser(self):
        print(self.name,self.age,self.email)

user1=User("Abhishek",26,"abhi.jais1211@gmail.com")
user2=User("vicky",25,"vicky.jais1211@gmail.com")
user1.getUser()
user2.getUser()