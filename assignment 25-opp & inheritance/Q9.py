class Truecaller:
    contact={"abhishek":7758938495,"vicky":8830274339}

    @classmethod
    def fetch(cls,key):
        print(cls.contact[key])

    @classmethod
    def add_contact(cls,key,value):
        cls.contact[key]=value
    @classmethod
    def getContact(cls):
        print(cls.contact)
user1=Truecaller()
print("Before adding contact")
Truecaller.getContact()
user1.add_contact("sarans",1234567890)
print("After adding contact")
Truecaller.getContact()
user1.fetch("sarans")