# opening tzop.txt in read mode, returning it as a file object
stream = open("tzop.txt", "rt", encoding = "utf-8")
# printing the content of the file
print(stream.read())
