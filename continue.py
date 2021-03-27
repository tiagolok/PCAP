largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")


# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Please input a word: ").upper()
for letter in userWord:
    # Complete the body of the for loop.
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    print(letter,end="\n")



wordWithoutVovels = ""

# Prompt the user to enter a word
# and assign it to the userWord = input("Please input a word: " variable
userWord = input("Please input a word: ").upper()

for letter in userWord:
    # Complete the body of the loop.
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue    
    wordWithoutVovels += letter
# Print the word assigned to wordWithoutVowels.
print(wordWithoutVovels)
