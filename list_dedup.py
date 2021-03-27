myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
for i in myList:
    if myList[i] in myList:
        del myList[i]

myList.sort()

print("The list with unique elements only:")
print(myList)
