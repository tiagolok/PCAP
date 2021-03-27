def anagrams(word1,word2):
    lst1 = sorted(list(word1.lower()))
    lst2 = sorted(list(word2.lower()))
    if lst1 == lst2:
        print("Anagrams")
    else:
        print("Not anagrams")
    
    # print(lst1,lst2)

anagrams('Listen','Silent')

anagrams('modern','norman')
