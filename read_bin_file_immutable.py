from os import strerror

try:
    bf = open('file.bin', 'rb')
##    data = bytearray(bf.read())
#   read 5 bytes each time
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerr(e.errno))
