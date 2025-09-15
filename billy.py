#starter program lesson 1
#name=input("what be thy name?")
#print("We want to know if you like programming!")
#print()
#answer = input("Do you like programming " + name + "?" )
#print("Great! You said ", answer, "!")
#print("Let's learn some Python today")
#the + are a standin for commas,
#harke ye need a plus to mix a var and sting it seems, me znaara

#name=input("what be thy name?")
#age=input("how many years have thee?")
#food=input("what have thou eaten last?")
#age=int(age)
#print("greetings mx.",name,"i hope thou hafth enjoyt thine",food,",","thou vvilt becometh",age+1,"in time coming, i vvish thee a happy early birthday")
#15 - 130 aaa jan dzoverr dzuvrujna hhalaa angdze

#character="j"
#ascii=ord(character)
#print(type(ascii))
#print(ascii)

# starter program week 2 - perhaps this could be a task

#def conversation():
#    print("Welcome to my conversation program")
#    print()
#    print("Do you like cycling? Answer \"yes\" or something else")
#    answer = input()
#    if answer=="yes":
#        print("That's good, you will get very fit")
#    else:
#        print("Perhaps you like some other sport. ")
#    print()
#    print("Goodbye")

#conversation()
#def says what the conversation is like var=var, naming the def and then () to indicate function makes it activate at any time 
#1st colon is for telling the computer to read the stuff after it to define the function, the else: defines a new function within the previous
#= is for vars and == is of ifs

#def conv2():
#    print("doch ryee liken feed?")
#    ans2=input("yay or nay?")
#    if ans2==("yay"):
#        print("dentvvi allen?")
#        print("heve nees dee")
#    elif ans2=="nay":
#        print("death be upon thee")
        
#conv2()

def qs():
    print("how many there be of the greater luminants? ")
    ansqs1=input("7, 8, 9 or 10? ")
    ansqs1=int(ansqs1)
    if ansqs1==7:
        print("indubitably")
        end1=1
    else:
        print("wrong, how could u possible be this foolish")
        end1=0
    print()
    
    print("how many be there of the shadow planets? ")
    ansqs2=input("2, 3, 4? ")
    ansqs2=int(ansqs2)
    if ansqs2==3:
        print("most definately")
        end2=1
    else:
        print("wrong, how dare thee misanswer")
        end2=0
    
    print()
    print("how strong be svarbhanu, in cents, to luna in core as compared to skin? ")
    ansqs3=input("1, 25, 50? ")
    ansqs3=int(ansqs3)
    if ansqs3==1:
        print("thou art wise")
        end3=1
    else:
        print("wrong, the phrasing vvas too easy for thee to fail")
        end3=0
    print()
    
    print("when jove doth leave the gate of the sun, when, of years, will in return once again? ")
    ansqs4=input("2, 12, 30? ")
    ansqs4=int(ansqs4)
    if ansqs4==12:
        print("how jovial thy preperation be")
        end4=1
    else:
        print("wrong, how saturnian of thee")
        end4=0
    
    print()
    print("in asumption all heavenly rings grow in their length, twain whomsts be rahuketu pulln the moon")
    ansqs5=input("sol and lun, lun and saturn, lun and jove, saturn and jove, martis and jove? ")
    ansqs5=str(ansqs5)
    if ansqs5=="saturn and jove":
        print("unshaded be thy shadow knowledge")
        end5=1
    else:
        print("wrong, aheined clefn")
        end5=0
    print()

    perfect=(end1+end2+end3+end4+end5)
    print(perfect, "/ 5")
    if perfect==5:
        print("alle be rixt, endless be thy wisdoms")

qs()
        
#def cooking():
#    print("(in french accent) Here be le menu")
#    print()
 #   print("1. Curry")
#    print("2. Bastilla")
#    print("3. Tklapi")
#    print()
#    answer=input("Vvic vvon ef rye feth dechrye desirran? (1, 2, 3 or none) ")
#    if answer == "1":
#        print("Curry coming up")
#        print("Enjoy!")
#    elif answer == "2":
#        print("Bastilla coming up")
#       print("Enjoy!")
#    elif answer=="3":
#        print("Tklapi coming up!")
#        print("Enjoy!")
#    elif answer=="none":
#        print("ye fell tasteless fuul")
#    else:
#        print("not an option :/")   
#cooking()
