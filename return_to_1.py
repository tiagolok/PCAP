step=0

c0 = int(input("Please input a random positive inetger : "))

while c0 != 1:
    if c0%2 == 0:
        c0 //= 2
        step += 1
        print(c0)
    else:
        c0 = 3*c0 + 1
        step += 1
        print(c0)
        
print("steps = ", step)
