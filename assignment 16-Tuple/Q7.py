tuple1=(1,2,3,4,5,6)
tuple2=()
for e in tuple1:
    if e==4 or e==5:
        tuple2+=(e,)
print(tuple2)
