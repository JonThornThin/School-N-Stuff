# Lesson 1 - Strings
# Worksheet 1
# Tier 1: Complete tasks 1-5 - check answers
# Tier 2: Complete tasks 6-9 - check answers
# Tier 3: Complete tasks 10-11 - check answers

#
# Tier 1 - Complete Tasks 1-5
#

course="LeavingCertComputerScience"

# Example completed for you:
#example = course[0:7]  # "Leaving"

# 1. Extract "Cert" (starts at position 7, ends at 11)
#print(course[7:11])
# 2. Extract "Computer" (starts at position 11, ends at 19)
#print(course[11:19])
# 3. Extract "Science" (starts at position 19, goes to end)
#print(course[19:])
# 4. Extract just the first letter "L"
#print(course[1-1])
# 5. Extract just the last letter "e"
#print(course[1])

# Tier 2 - Complete Tasks 6-9

# 6. Extract every 2nd character starting from the beginning
print(course[::2])  # Hint provided
# 7. Extract the last 7 characters
print(course[-7:])
# 8. Reverse the entire string
print(course[::-1])
# 9. Extract "LCC" (first letters of each word - tricky!)
# Hint: Positions are 0, 7, 11
print(course[0],course[7],course[10])


# Tier 3 - Complete Tasks 10-11

# 10. Extract characters in positions 2, 5, 8, 11 
print(course[2],course[5],course[8],course[11])

# 11. Get every third character from the end
print(course[::-3])