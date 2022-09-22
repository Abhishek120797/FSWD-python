import keyword
count=0
with open("Q7.py",'r') as py_file:
    for line in py_file.readlines():
        for word in line.split(' '):
            if word in keyword.kwlist:
                print(word)
                count+=1
print("{} python keyword present in {} file".format(count,py_file.name))

