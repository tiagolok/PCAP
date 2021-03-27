def mysplit(strng):
    lst = []
    word = ''
    
    for i in range(len(strng)):
        if strng[i] != " ":
            word += strng[i]
        else:
            if word != '':
                lst.append(word)
            word = ''
    if word != '':
        lst.append(word)   
        
    return lst
    
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
