# my_list = ["Apple", "Orange"]
# print(len(my_list))

# my_dict = { 'apples': 23, 'oranges': 32, 'pears': 21 }

# print(my_dict['apples']) # => 23
# my_dict['oranges'] # KeyError: 'kiwi'

# if "apples" in my_dict:
#   print("We got apples!")

# my_list = ["Cat", "Mouse", "Frog"]
# my_list.remove("Mouse")
# my_list.insert(0, "Mouse")
# my_list.insert(1,"Lynx")
# print(my_list)

my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog", "Horse"]
counters = {}

# Write some code to count the items in the list here
for animal in my_list:
  changed_animal = animal.lower()

  if changed_animal in counters:
    counters[changed_animal]= counters[changed_animal] + 1
  else:
    counters[changed_animal] = 1
print(counters)
# Should print (in any order)
# { 'cat': 3, 'dog': 2, 'frog': 1 }


 # Put the names of the people in your cohort here

# Program should print a dictionary with each of the letters of the alphabet
# and the number of people whose first name begins with that letter.
# E.g. { 'a': 2, 'b': 0, ... }
my_cohort = ["Sapna", "Sonali", "Jonnah", "Krysten"]
counters = {}

for name in my_cohort:

  if name[0] in counters:
    counters[name[0]]= counters[name[0]] + 1
  else:
    counters[name[0]] = 1
print(counters)