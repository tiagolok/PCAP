def palindrome(word):
    word = word.lower().replace(' ','')
    # print(word)
    word_reverse = ''
    for i in range(len(word)):
        word_reverse += word[len(word)-i-1].lower()
    # print(word_reverse)
    if word_reverse == word:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

palindrome("Ten animals I slam in a net")
palindrome("Eleven animals I slam in a net")
