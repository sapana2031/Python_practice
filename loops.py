# num = 1
# while num < 10:
#   print(num)
#   num = num + 1
# # Prints the numbers 1 through 9

# for num in range(1, 10):
#   print(num)

# for name in ["Sapna", "Sona"]:
#   print(name)

#Write a program to print all the numbers from 2321 to 34325 inclusive.
# for num in range(2321, 34326):
#   print(num)

#Write a program to sum all of the even numbers in that range.

# total = 0
# for num in range(1, 10):
#   if num % 2 == 0:
#     total += num
# print(total)
from math import factorial


total = 0
for num in range(2321, 34325):
  if num % 2 == 0:
    total += num
print(total)

# Write a program to find the factorial of 17.

# The factorial of a number is that number multiplied by every number below it until 1. So, 10 factorial is 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1, evaluating to 3628800.---When correct, your program should produce the number 355687428096000.--- for this you need --from math import factorial

num = 17
print ("Factorial of", num,"is",factorial(num))