def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)


def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)
