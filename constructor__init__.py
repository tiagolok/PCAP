class Classy:
    def __init__(self, value = None):
        self.var = value

obj1 = Classy("object")
obj2 = Classy()

print(obj1.var)
print(obj2.var)
