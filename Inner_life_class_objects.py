class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

print('obj.var: ', obj.var, 'obj.varia: ', obj.varia)

print('Classy.varia: ', Classy.varia)

if hasattr(Classy, 'var'):
    print(Classy.var)
else:
    print('Classy.var does not exist')
