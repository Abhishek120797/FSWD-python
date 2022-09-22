city_list_2=['Shimla','pune','Lucknow']
with open("cities.txt",'a') as f:
    for city in city_list_2:
        f.write(city)
        f.write('\n')
