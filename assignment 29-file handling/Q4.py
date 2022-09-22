city_list=['Mumbai','Jaipur','Surat','Jaunpur','Banaras','Rampur']
with open("cities.txt",'w') as f:
    for city in city_list:
        f.write(city)
        f.write('\n')
        
        
