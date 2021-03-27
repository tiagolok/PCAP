from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
##    ch = s.read(1)
##  read the whole file to the memory at once
    content = s.read()
##    while ch != '':
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
