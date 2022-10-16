class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showconfig(self):
        print(self.brand,self.ram,self.cpu,self.hdd)

com1=Laptop("dell",8,"i5",500)
com1.showconfig()