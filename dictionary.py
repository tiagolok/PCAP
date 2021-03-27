dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
# keys are case-sensitive: 'Suzy' is something different from 'suzy'.
print(phone_numbers['Suzy'])


# And now the most important news: you mustn't use a non-existent key.
# Trying something like this:
print(phone_numbers['president'])

# The following code safely searches for some French words:
dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
