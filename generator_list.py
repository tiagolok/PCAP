def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2

t = [x for x in powersOf2(5)]

print(t)

t = list(powersOf2(3))

print(t)

for i in range(20):
    if i in powersOf2(4):
        print(i)
