with open("demo.txt","w") as f:
    f.write("My name is Abhishek Jaiswal")
print("file is read only") if f.mode=='r' else print("file is not read only")
print("file is closed") if f.closed else print("file is opened")
print("file mode is {}".format(f.mode))
print("file name is {}".format(f.name))
input()
