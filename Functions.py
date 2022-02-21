def greet(name):
  return f'Hello, {name}!'
print(greet("Sapna"))
# Your code goes here.
def add_five(num):
  return num + 5
print(add_five(4))

print(add_five(2132))
# Should print: "2137"

def subtract_low_from_high(num1, num2):
  if num1 < num2:
    return num2 - num1
  else:
    return num1 - num2
  
print(subtract_low_from_high(2, 3))
# Should print "1"

print(subtract_low_from_high(3, 2))
# Should print "1"

print(add_five(subtract_low_from_high(1463, 16475)))
# Should print "15017"

# Write a method called superify which takes a string and adds the word "super" to the start. So given 'woman' it returns 'superwoman', given 'dog' it returns 'superdog'.


def superify(str):
  return "super" + str
print(superify(superify(superify(superify("cat")))))
