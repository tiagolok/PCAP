largestNumber = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")


counter  = 0

while True:
    word = input("Enter a word or type exit to end the program: ")
    if word == "exit":
        break
    elif word != "chupacabra":
        counter += 1
    else: 
        counter += 1
        break

if counter != 0:
    print("You've successfully left the loop.")
else:
    print("You haven't entered any word.")

        
