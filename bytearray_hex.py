# not allowed to assign a value that doesn't come from the range 0 to 255 inclusive
data = bytearray(255)

for i in range(len(data)):
    data[i] = 255 - i

for b in data:
    print(b,hex(b))
