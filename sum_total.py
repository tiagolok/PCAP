# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0

try: 
    strings.isspace()

    try:
        for substr in strings:
            total += float(substr)
        print("The total is:", total)
    except:
        print(substr, "is not a number.")

except:
    print("You did not input any numbers!")
