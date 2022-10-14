def count(str_a):
    lower_case=0
    upper_case=0
    for e in str_a:
        if e.islower():
            lower_case+=1
        if e.isupper():
            upper_case+=1
    print("lowercase later = {}".format(lower_case))
    print("uppercase later = {}".format(upper_case))
    
str_1=[e for e in input("Enter first string : ")]
count(str_1)
