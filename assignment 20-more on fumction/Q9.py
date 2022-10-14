def pangram(set_2):
    a_to_z=[e for e in "abcdefghijklmnopqrstuvwxyz"]
    for e in a_to_z:
        if e not in set_2:
            print("string is not pangram")
            break
    else:
        print("string is pangram")
            
set_1={e for e in input("Enter a string : ").lower() if e!=' '}
pangram(set_1)
