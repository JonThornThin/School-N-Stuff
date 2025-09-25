#eterh leemoe

#coke=4*1.5 #these 5 calculate the costs unit*€cost
#bars=1*5
#crisps=0.8*3
#tea=2*2
#bread=3.5
#print("the total is €", coke+crisps+bars+tea+bread) #this ADDS THE COSTS TOGTHER AND STATES IT AT THE END A OF A STRING

#print()
#num1=int(input("whats the 1st number? ")) #these do be ask what the variables be 
#num2=int(input("whats the 2nd number? "))
#sum=num1+num2 # adds the vars
#print(num1, "+", num2, "=", sum) #prints the sum along with the result

#print()
#C=int(input("whats the celcius? "))
#NoTriFract=5/9 #this exists to avoid a triple layer fracton which the computer really doesnt like
#F=C/NoTriFract+32
#roundF=round(F, 2)
#print(roundF, "in farenheit")

#print()
print("this is a program which tells u the weekday based of any date")
print()
dd=int(input("what was the date of the month? (e.g. 1st of april is 1) "))
mmb=int(input("what was the month of the year? (e.g. March is 3) "))
if mmb==1:
    mm=mmb+12
elif mmb==2:
    mm=mmb+12
else:
    mm=mmb
c=int(input("what was the century? (e.g. 2025 is 20) "))
y=int(input("what was the year of the century? (e.g. 2025 is 25) "))
A=(13*(mm+1))/5
wb=dd+A+y+(y/4)+(c/4)-(2*c)
w=wb%7
print(w)
