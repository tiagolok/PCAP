def outer(par):
    loc = par

var = 1
outer(var)

print(var)
print(loc)

# The last two lines will cause a NameError exception
# neither par nor loc is accessible outside the function.
# Both the variables exist when and only when the outer() function is being executed
