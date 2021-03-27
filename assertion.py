from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# we must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
