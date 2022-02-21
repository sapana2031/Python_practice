switch = False

if switch:
  print("Switch is true")
else:
  print("Switch is false")

print("This always runs")

print(2>1)
print(2 >= 3)

import random

random_number = random.randint(1, 5)
if random_number > 2:
  print("More")
elif random_number == 2:
  print("Two")
else:
  print("One")


import time

seconds = int(time.time())

if seconds % 3 == 0 :
  print("Fizz")
elif seconds % 5 == 0:
  print("Buzz")
elif seconds % 15 == 0:
  print("FizzBuzz")
else:
  print(seconds)
