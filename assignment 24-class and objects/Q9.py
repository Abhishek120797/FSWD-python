class School:
    board="Maharashtra"
    def __init__(self,name,grade,location):
        self.name=name
        self.grade=grade
        self.location=location
    def showSchool(self):
        print(self.name,self.grade,self.location)

school1=School("lokmanya school","primary","miraroad")
school1.showSchool()
print(school1.board)