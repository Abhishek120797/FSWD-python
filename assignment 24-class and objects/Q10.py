class Employee:

    def __init__(self,empid='\0',name='\0',salary='\0'):
        self.empid=empid
        self.name=name
        self.salary=salary

    def input(self):
        self.empid=int(input("Enter empid : "))
        self.name=input("Enter your name : ")
        self.salary=int(input("Enter your salary : "))
    
    def display(self):
        print(self.empid,self.name,self.salary)

emp1=Employee(1,"abhishek jaiswal",12000)
emp2=Employee()
emp2.input()
emp1.display()
emp2.display()