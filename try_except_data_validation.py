def readint(prompt, min, max):
    Entry = True
    while Entry:
        try:
            x = int(input("Enter a number from -10 to 10: "))
            assert -10 <= x <= 10
            retry = False 
            return x
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (",min,"..",max,")",sep="")
        
v = readint("Enter a number from -10 to 10: ", -10, 10)      
print("The number is:", v)

