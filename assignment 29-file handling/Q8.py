with open("cities.txt",'r') as f:
    text=f.read()
    with open("copy_cities.txt",'w') as c_f:
        c_f.write(text)
