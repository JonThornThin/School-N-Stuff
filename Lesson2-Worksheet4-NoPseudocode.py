# Lesson 2 - Strings
# Worksheet 4
# Problem: Create a username validator

print("make me a password")
print()
print("Must be:")
print("Between 5-15 characters")
print("Only letters and numbers")
print("Must start with a letter")
print()
pw=str(input())
print()
lpw=pw.lower()
right=0

#checking for right length

countright=0
charcount=0
for char in pw:
    charcount+=1
if charcount>15:
    print("too long")
elif charcount<5:
    print("too short")
else:
    countright=1

#checking for only letters and numbers

letandnum="1234567890qwertyuiopasdfghjklzxcvbnm"
letandnumwrong=0
letandnumright=0
for char in lpw:
    if char not in letandnum:
        letandnumwrong=1 #made this number cause itd print the dissallowed char message once for every char
    else:
        letandnumright=1
if letandnumwrong==1:
    print("this password has a disallowed character")

#checking start letter

letter="qwertyuiopasdfghjklzxcvbnm"
start=(lpw[0])
startright=0
if start not in letter:
    print("the start of the password must be a letter")
elif start in letter:
    startright=1
    
#checking all right 

if letandnumright==1:
    right+=1
if countright==1:
    right+=1
if startright==1:
    right+=1

print()
if right==3:
    print("everything seems good!")
else:
    print("please try another password")