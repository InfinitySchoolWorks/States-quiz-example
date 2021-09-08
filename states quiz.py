# Inputs
name = input("Enter your name: ")   # Asks for name
points = 0  # This is the intial points value we will add one for each question

# Program
tn = (input("Enter the capital of Tamil Nadu: ")).lower()     # gets an input and makes all characters in lower case
if tn == "chennai" or tn == "madras":                       # checks if its the correct ans and the 'or' is there if the user is kinda old
    print("Your answer is correct!")                        # This actually optional, if you only want to show points at end and don't want to show which went wrong then only increment point
    points += 1                                             # This is essentialy saying points + 1 = points, you add 1 to points

else:
    print("Your answer was wrong")                          # If the input is anything except 'chennai' or 'madras' it will execute this

# Finally after fininshing the processing

print(name, "scored", points,"out of 10")                   # 10 if you are not lazy like me and did just one for example
