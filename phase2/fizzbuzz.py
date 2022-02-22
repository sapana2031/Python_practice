# CALLING:
#   fizzbuzz(15)
# SHOULD RETURN:
#   "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz"

def generate(upto):
  print("hhhh")
  return "1"
  
def fizzbuzz(i):
  if i % 15 == 0:
    return "FizzBuzz"
  elif i % 3 == 0:
    return "Fizz"
  elif i % 5 == 0:
    return "Buzz"
  else:
    return i
print(fizzbuzz(8))
