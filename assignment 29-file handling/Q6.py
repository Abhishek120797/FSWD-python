check_city=input("Enter a city name : ")
with open("cities.txt",'r') as f:
    try:
        city_list=f.read().split("\n")
        for city in city_list:
            if city.lower()==check_city.lower():
                print("{} exist in {} file".format(check_city,f.name))
                break
        else:
            print("{} not exist in {} file".format(check_city,f.name))
    except FileNotFoundError:
        print("FIle not found")
    
    
    
