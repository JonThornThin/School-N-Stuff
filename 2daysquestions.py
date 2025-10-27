def section1():
    var="hi"
    print(type(var))

    year=int(input("what year were u born? "))
    print("ur about",2025-year,"or", 2024-year, "years old")

    print()
    num1=int(input("tell me a number "))
    num2=int(input("and another "))
    print("sum = ", num1+num2)
    print("difference = ", num1-num2)
    print("product = ", num1*num2)
    print("division = ", num1/num2)
    print("floor div. = ", num1//num2)
    print("remainder = ", num1%num2)
    print("power = ", num1**num2)

def section2():
    #2.1
    charcount=0
    sentance=input("tell me something (with space pleeeeeeeease) ")
    print(sentance.upper())
    print(sentance.lower())
    for char in sentance:
        charcount+=1
    print(charcount, "chars")
    print("space in position",1+sentance.find(" "))
    print(sentance.replace(" ", "_"))
    
    
    #2.2
    print()
    print("use atleast 8 chars")
    print("use at least one digit")
    pw=input("make me a password! ")
    print()
    
    #checks length
    #these bring the count to start to 0
    lenright=0
    if len(pw)<8:
        print("make sure its 8 chars or longer")
    else:
        lenright=1
        
    #checks digit need
    digitright=0
    for char in pw:
        if char.isdigit():
            digitright=1
            break #stops the for-loop
    if digitright==0:
        print("it needs atleast one digit")
    
    #checks if all is right
    if lenright+digitright==2:
        print("all's right!")


"""
input words
lower word
count letter
find first and last space
extract whats before first and last space
replace ieaou with *
"""
def sec2_3():
    print()
    print()
    wrds=input("tell me a few words ")
    print()
    lwrds=wrds.lower()
    acnt=0
    for char in lwrds:
        if char=="a":
            acnt+=1
    print("there're", acnt, "A's")
    
    print("the first word is \""+ wrds[0:wrds.find(" ")] + "\"") #the plus concatonates the comas together
    
    rwrds=wrds[::-1] #revrses the word
    nwrds=rwrds[0:rwrds.find(" ")] #finds the first word backwards
    print("the last word is \""+ nwrds[::-1] +"\"") #reverses this word just found
    
    print("ok now ima cencor the vowels", wrds.replace("i","*").replace("e","*").replace("a","*").replace("o","*").replace("u","*").replace("I","*").replace("E","*").replace("A","*").replace("O","*").replace("U","*"))
            
def grading():
    gr=int(input("what grade did u get 0-100% "))
    if gr>100:
        print("thats suspiciosly high")
    elif 101>gr>89:
        print("u got an A")
    elif 91>gr>79:
        print("u got a B")
    elif 81>gr>69:
        print("u got a C")
    elif 71>gr>59:
        print("u got a D")
    elif 61>gr>-1:
        print("u got an F")
    else:
        print("how did u fail that bad")
    
def leapyear():
    yr=int(input("whats the year? "))
    if yr%4==0: #by checking for a remainder i am checking if smn is an int
        if yr%100==0:
            if yr%400==0: #if divisable by 4, 100 and 400 is leap 
                print("das a leap year")
            else: #if is div by 4 and 100 but not 400 is not leap
                print("not a leap year")
        else: #if div by 4 but not 100 is leap
            print("das a leap year")
    else: #if not div by 4 not leap
        print("not a leap year")




#section1()
#section2()
#sec2_3()
#grading()
#leapyear()
        
#print(isinstance(int(4.0), int))