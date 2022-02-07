my_dictionary = {1: "L.A. Lakers", 2: "Houston Rockets", 3: "Dallas Mavericks"}
print(my_dictionary)

# get() method
print(my_dictionary.get(2))
print(my_dictionary.get(4))

# dictionary key-value methods
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

# access and write data
my_dictionary[1] = "Los Angeles Clippers"
print(my_dictionary)

# update dictionary
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}
dict1.update(dict2)
print(dict1)

# pop()
popped = my_dictionary.pop(1)
print(popped)
print(my_dictionary)