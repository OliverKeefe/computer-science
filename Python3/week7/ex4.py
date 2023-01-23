print ("This program finds all indexes of a character in a string.\n") 
inStr = input("Enter a string to search:\n") 
searchChar = input("\nWhat character to find? ") 
searchChar = searchChar[0] # make sure only one char!
anyFound = False # flag to indicate if char found
startAt = 0 
index = startAt 

while index < len(inStr): 
    if inStr[index] == searchChar: 
        anyFound = True
        if anyFound == True:
            print ("'" + searchChar + "' found at index", index) 
    index = index + 1 

if anyFound == False: 
    print ("Sorry, no occurrences of '" + searchChar + "' found.") 

# FIXED! Woo!

