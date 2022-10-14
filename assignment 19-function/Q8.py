def multilist(a):
    multi=1
    for e in a:
        multi=multi*e
    print("multiplication of list1 elements is {}".format(multi))
list1=[1,2,3,4]
multilist(list1)
