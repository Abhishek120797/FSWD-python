decimal = int(input("Enter a decimal number : "))
binary = 0
ctr = 0
while(decimal > 0):
    binary = ((decimal%2)*(10**ctr)) + binary
    decimal = int(decimal/2)
    ctr += 1   
print(binary)
