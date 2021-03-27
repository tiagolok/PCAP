class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

# try:
#    print(exampleObject.b)
# except AttributeError:
#    pass

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)
