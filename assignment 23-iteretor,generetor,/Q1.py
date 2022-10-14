set_1={1,2,3,4,5,6,7,8,9,10}
set_obj=iter(set_1)
i=0
while i<10:
    print(next(set_obj),end=" ")
    i+=1
