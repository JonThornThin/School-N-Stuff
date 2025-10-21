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
    pwcount=0 #these bring the count to start to 0
    right=0
    print("use atleast 8 chars")
    print("use at least on digit")
    pw=input("make me a password! ")
    
    #checks length
    for char in pw: #count +1 for each character
        pwcount+=1
    if pwcount<8:
        print("make sure its 8 chars or longer")
    else:
        right+=1
        
    #checks digit need
    for char in pw:
        if char.isdigit():
            right+=1
            break #stops the for loop after proven boolean
        else:
            print("it needs atleast one digit")
            break
    if right==2:
        print("all's right!")


#section1()
section2()