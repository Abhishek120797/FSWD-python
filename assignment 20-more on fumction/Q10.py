def anagram(str_a,str_b):
    if len(str_a)!=len(str_b):
        print("strings are not anagram")
    else:
        for e in str_a:
            if e not in str_b:
                print("strings are not anagram")
                break
        else:
            print("strings are anagram")

str_1=[e for e in input("Enter first string : ").lower()]
str_2=[e for e in input("Enter second string : ").lower()]
anagram(str_1,str_2)
