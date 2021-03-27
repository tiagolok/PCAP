from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # actual processing goes here
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno));
