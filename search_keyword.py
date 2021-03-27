def search_string(word1,word2):
    lst1 = list(word1.lower())
    lst2 = list(word2.lower())
    
    i,j = 0,0
    wrd1,wrd2 = '', ''
    while i in range(len(lst1)):
        if lst1.count(lst1[i]) > 1:
            del lst1[i]
        i += 1

    while j in range(len(lst2)):
        if lst2.count(lst2[j]) > 1:
            del lst2[j]
        j += 1

    lst1.sort()
    lst2.sort()
    
    for str1 in lst1:
        wrd1 += str1
    for str2 in lst2:
        wrd2 += str2
    
    print(wrd1, wrd2)
    
    if wrd2.find(wrd1) > 0:
        print("Yes")
    else:
        print("No")
    

search_string('donor','Nabucodonosor')
search_string('donut','Nabucodonosor')
