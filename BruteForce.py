def bruteForce():
	pass

# Reading config
f = open("Cases.config", "r") 
characters = f.readline().strip() # characters to be taking into account
passwordLengthNumberToBegin = int(f.readline()) # min password length to test
passwordLengthNumberToEnd = int(f.readline()) # max password length to test

# Creating character to index correspondancies for ligther performance
charToIndex = {}
maxCharIndex = 0
for c in characters:
    charToIndex[maxCharIndex] = c
    maxCharIndex += 1
maxCharIndex -= 1
if passwordLengthNumberToBegin == 0:
    print("Password min length 0")
    exit()

if passwordLengthNumberToEnd == 0:
    print("Password max length 0")
    exit()

if passwordLengthNumberToBegin > passwordLengthNumberToEnd:
    print("2nd line of config is for min passwd length. 3rd is for max passwd length.")
    exit()

bruteForce(passwordLength, chars, hash)
