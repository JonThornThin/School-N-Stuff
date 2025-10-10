# Lesson 2 - Strings
# Worksheet 3
# Tier 1: Complete tasks 1-2 - check answers
# Tier 2: Complete tasks 3-4 - check answers
# Tier 3: Complete tasks 5 - check answers

#
# Tier 1 - Complete Tasks 1-2
#

# Task 1: Count vowels in a word
#text = "algorithm"
vowel = "ieaou"
#vowel_count = 0

# Complete this code
#for letter in text:
#    if letter in vowel:
#        vowel_count = vowel_count +1 # Add 1 to the count
    
#print("Vowels found:", vowel_count)

# Task 2: Now try with a different word:
text2 = "khaal tali gama"
vowelcount2 = 0
for letter in text2:
    if letter in vowel:
        vowelcount2+=1
print(vowelcount2)



print()
print()
#Tier 2 - Complete Tasks 3-4


# Task 3: Count PLOSIves
textp = "PROgramming"
plosive = "ptkbdgPTKBDG"
plosivecount = 0
for textp in textp:
    if textp in plosive:
        plosivecount+=1
print(plosivecount)

# Task 4: Count how many uppercase and lowercase letters separately
lvngcrt = "LeavingCert"
lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
uppercount = 0
lowercount = 0
for letter in lvngcrt:
    if letter in lower:
        lowercount+=1
print("lower", lowercount)

lvngcrt = "LeavingCert" #i dont know why but if u dont restate this it starts at the final letter
for letter in lvngcrt:
    if letter in upper:
        uppercount+=1
print("upper",uppercount)

# Write your code here:

print()
print()
#
# Tier 3 - Complete Tasks 5
#

# Task 5: Create a character frequency counter
algo=input(str("tell me somthing ill count the letters! "))
algo=algo.lower()
acount=0
for letter in algo:
    if letter=="a":
        acount+=1
bcount=0
for letter in algo:
    if letter=="b":
        bcount+=1
ccount=0
for letter in algo:
    if letter=="c":
        ccount+=1
dcount=0
for letter in algo:
    if letter=="d":
        dcount+=1
ecount=0
for letter in algo:
    if letter=="e":
        ecount+=1
fcount=0
for letter in algo:
    if letter=="f":
        fcount+=1
gcount=0
for letter in algo:
    if letter=="g":
        gcount+=1
hcount=0
for letter in algo:
    if letter=="h":
        hcount+=1
icount=0
for letter in algo:
    if letter=="i":
        icount+=1
jcount=0
for letter in algo:
    if letter=="j":
        jcount+=1
kcount=0
for letter in algo:
    if letter=="k":
        kcount+=1
lcount=0
for letter in algo:
    if letter=="l":
        lcount+=1
mcount=0
for letter in algo:
    if letter=="m":
        mcount+=1
ncount=0
for letter in algo:
    if letter=="n":
        ncount+=1
ocount=0
for letter in algo:
    if letter=="o":
        ocount+=1
pcount=0
for letter in algo:
    if letter=="p":
        pcount+=1
qcount=0
for letter in algo:
    if letter=="q":
        qcount+=1
rcount=0
for letter in algo:
    if letter=="r":
        rcount+=1
scount=0
for letter in algo:
    if letter=="s":
        scount+=1
tcount=0
for letter in algo:
    if letter=="t":
        tcount+=1
ucount=0
for letter in algo:
    if letter=="u":
        ucount+=1
vcount=0
for letter in algo:
    if letter=="v":
        vcount+=1
wcount=0
for letter in algo:
    if letter=="w":
        wcount+=1
xcount=0
for letter in algo:
    if letter=="x":
        xcount+=1
ycount=0
for letter in algo:
    if letter=="y":
        ycount+=1
zcount=0
for letter in algo:
    if letter=="z":
        zcount+=1
othercount=0
alpha="qwertyuiopasdfghjklzxcvbnm"
for letter in algo:
    if not letter=="alpha":
        othercount+=0
print("a", acount,"b", bcount,"c", ccount)
print("d", dcount,"e", ecount,"f", fcount)
print("g", gcount,"h", hcount,"i", icount)
print("j", jcount,"k", kcount,"l", lcount)
print("m", mcount,"n", ncount,"o", ocount)
print("p", pcount,"q", qcount,"r", rcount)
print("s", scount,"t", tcount,"u", ucount)
print("v", vcount,"w", wcount,"x", xcount)
print("y", ycount,"z", zcount, "&", othercount, "nonletters")
# Your output should look like this:
# a: 1
# l: 1
# g: 1
# o: 1
# r: 1
# i: 1
# t: 1
# h: 1
# m: 1

# Hint: You might want to use a dictionary or count each letter individually