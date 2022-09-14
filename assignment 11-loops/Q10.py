decimal = int(input("Enter a decimal number : "))
binary = 0
ctr = 0
while(decimal > 0):
    binary = ((decimal%8)*(10**ctr)) + binary
    decimal = int(decimal/8)
    ctr += 1   
print(binary)
