class Account:
    def __init__(self,id,bal):
        self.id=id
        self.bal=bal

    def __add__(self,obj2):
        result=Account(0,0)
        result.id=self.id+obj2.id
        result.bal=self.bal+obj2.bal
        return result
    
    def getaccount(self):
        print(self.id,self.bal)
    
    def __str__(self):
        return str(self.id)+':'+str(self.bal)

user1=Account(201,1000)
user2=Account(202,2000)
user3=Account(203,3000)
sum=user1+user2+user3

print(user1)