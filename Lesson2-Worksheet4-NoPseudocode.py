# Lesson 2 - Strings
# Worksheet 4
# Problem: Create a username validator

attempt=0
def password(attempt):
    pw=str(input("enter:   "))
    lpw=pw.lower()
    right=0
    
    #checking for right length

    countright=0
    charcount=0
    for char in lpw:
        charcount+=1
    if charcount>15:
        print("too long")
    elif charcount<5:
        print("too short")
    else:
        countright=1

    #checking for only letters and numbers

    letandnum="1234567890qwertyuiopasdfghjklzxcvbnm"
    letandnumright=0
    for char in lpw:
        if char not in letandnum:
            print("this password has a disallowed character")
            break
        else:
            letandnumright=1

    #checking start letter

    letter="qwertyuiopasdfghjklzxcvbnm"
    startright=0
    if (lpw[0]) not in letter:
        print("the start of the password must be a letter")
    elif (lpw[0]) in letter:
        startright=1
    
    #checking all right

    right=letandnumright+countright+startright

    print()
    if right==3:
        print("everything seems good!")
        attempt=0
        return attempt
    else:
        attempt+=1
        return attempt

print("make me a password")
print()
print("Must be:")
print("Between 5-15 characters")
print("Only letters and numbers")
print("Must start with a letter")
print()
print("you have 3 attemps")


def attempts(attempt):
    if password(0)==1:
        print("2 attempts left, try again")
    else:
        return
    if password(1)==2:
        print("1 attempts left, try again")
    else:
        return
    if password(2)==3:
        print("youre going to prison forever now >:(")

attempts(attempt)