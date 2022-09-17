def puzzel(word,random):
    puzzel_char=[e for e in random]
    print(puzzel_char)
    if input("Form a valid word using this letters : ").upper()==word:
        print("correct")
        return 1
    else:
        print("Wrong")
        print("correct is '{}'".format(word))
        return -1

def play():
    word_dict=dict(FATHER="TERAFH",AEROPLANE="AENOPAREL",GREEN="RENEG",FOOTBALL="TALLOOFB",BREAK="KABRE",CTRAOTR="TRACTOR",PLEASE="PELESA",CHAIR="RIHAC",GROUND="ROGUDN")
    score=0
    i=1
    for e in {v for v in word_dict.keys()}:
        if i<=5:
            print("Round >>>",i)
            score+=puzzel(e,word_dict[e])    #function call
            print("your score {}".format(score))
            print()
        else:
            print("******Game over******")
            print("Hey! {} [your Total score = {}]".format(name,score))
            if int(input("want to play again Enter '1' for quit Enter '0'")):
                play()   #function call
            else:
                break
        i+=1

print("Welcome to the ***word puzzel game***")
name=input("Enter player name : ")
print()
print("Hey! {} please read game rule carefully".format(name))
print()
print("******Rules******")
print("1:Five rounds we will going to play ")
print("2:for each round form a correct word each correct word 1 point added to your total score")
print("3:For each round if you form a wrong word -1 point added to your total score")
print()
input("Enter any key to begin the GAME : ")
play()
