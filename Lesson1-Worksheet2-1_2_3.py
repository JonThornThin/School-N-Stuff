# Lesson 1 - Strings
# Worksheet 2
# Tier 1: Complete tasks 1-5 - check answers
# Tier 2: Complete tasks 6-10 - check answers
# Tier 3: Complete tasks 11-13 - check answers

text = "Python Programming"
print(text)
# Use your Reference Guide to help!

#
# Tier 1 - Complete Tasks 1-5
#

# 1. Convert to all uppercase
print(text.upper())

# 2. Convert to all lowercase  
print(text.lower())

# 3. Count how many times 'o' appears
print(text.count('o'))

# 4. Replace 'Python' with 'Java'
print(text.replace('Python', 'Java'))

# 5. Find the position where 'gram' starts
print(text.find('gram'))

text = "Python Programming"

#
# Tier 2 - Complete Tasks 6-10
#

# 6. Check if the entire string is lowercase
print(text.islower())

# 7. Check if the entire string is uppercase
print(text.isupper())

# 8. Replace all spaces with underscores
print(text.replace(" ", "_"))

# 9. Count how many times the letter 'P' appears (case-sensitive)
print(text.count("P"))

# 10. Create a new string that says "I love Python Programming"
print("I love", text)


#
# Tier 3 - Complete Tasks 11-13
#

messy = "   PyThOn@123   "

# 11. Clean this input: remove spaces, make lowercase,
messy=messy.replace(" ", "")
print(messy)
messy=messy.lower()
print(messy)
messy=messy.replace("@","")
print(messy)
# You'll need multiple methods!

# 12. Check if a string contains ONLY letters (no numbers or spaces)
test_string = "PythonProgramming"
print(test_string.isalpha())
# 13. Create a function that takes any text and returns the number of words (hint: count spaces + 1)
#said=input("tell me something, ill count the words! ")
#print(said)
print()
print()
print()
exmp="Example"
print(exmp)
print()
#x.replace replaces one value with another
print(exmp.replace("le","ulation"))
#can also be used for removals
print(exmp.replace("xampl",""))

#x.islower and x.isupper check for full lower and upper case
print(exmp.isupper())
print(exmp.islower())
#both return false as the input isnt pure of its case

#x.isalpha and x.isdigit check for only letter or only numbers
print(exmp.isalpha())
#alpha has nothing to do with alphabeticl order
print(exmp.isdigit())
#alpha retruns true and digit returns false