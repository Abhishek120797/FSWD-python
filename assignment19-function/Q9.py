def check(a,range_1):
   print("number found") if a in range_1 else print("number not found")        
y=range(int(input("enter range value : "))+1)
x=int(input("Enter a number : "))
check(x,y)
