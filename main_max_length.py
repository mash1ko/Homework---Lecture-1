x = 0
myList = []
# ask user input

while x < 5:
    userInput = input("Enter word: \n")
    x = x + 1
    myList.append(userInput)
    
# choose and print max length string

print(len(max(myList, key=len)))



