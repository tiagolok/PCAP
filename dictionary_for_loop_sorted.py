dictionary = {"cat" : "chat", "horse" : "cheval", "dog" : "chien"}

for key in sorted(dictionary.keys()):
# for key in dictionary.keys():
    print(key, "->", dictionary[key])

# The method returns tuples where each tuple is a key-value pair.
for english, french in dictionary.items():
    print(english, "->", french)

# There is also a method named values(), which works similarly to keys(), but returns values.
for french in dictionary.values():
    print(french)
