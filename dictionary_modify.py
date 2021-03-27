dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}


# dictionaries are fully mutable
dictionary['cat'] = 'minou'
print(dictionary)

# assign a value to a new, previously non-existent key
dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"duck" : "canard"})
print(dictionary)


# removal of the associated value. Values cannot exist without their keys.
del dictionary['dog']
print(dictionary)

# To remove the last item in a dictionary
dictionary.popitem()
print(dictionary)    # outputs: {'cat' : 'chat', 'dog' : 'chien'}
