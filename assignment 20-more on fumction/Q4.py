def palindrome(str_2,n):
    i=0
    j=-1
    while(i<n):
        if str_2[i]!=str_2[j]:
            print("enterd string is not palindrome")
            break
        j-=1
        i+=1
    else:
        print("enterd string is palindrome")
          
str_1=[e for e in input("Entera string : ").upper()]
palindrome(str_1,len(str_1))
