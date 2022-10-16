class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showconfig(self):
        print(self.brand,self.ram,self.cpu,self.hdd)

com1=Laptop("Dell",8,"i5",512)
com2=Laptop("Asus",4,"i3",256)
com3=Laptop("HP",16,"i9",1024)
my_class_list=[com1,com2,com3]
my_class_list.sort(key=lambda x:x.ram)
for i in my_class_list:
    i.showconfig()