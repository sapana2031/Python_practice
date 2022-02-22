# class Greeter:
#   def __init__(self, name):
#     self.name = name
#   def greet(self):
#     return f'Hello, {self.name}!'

# greeter = Greeter("Sapna")
# print(greeter.greet())

# #Create an Introducer class that has two methods, announce and introduce.
# class Introducer:
#   def __init__(self, name):
#     self.name = name
  
#   def announce(self):
#     return f'I am, {self.name}!'
  
#   def introdue(self, name):
#     return f'Hello, {name}, I am {self.name}! '

#   def hello(self, name, name1):
#     return f'Hi , {name}, {name1}, {self.name}! '

# introducer = Introducer("Kay")
# print(introducer.announce())
# print(introducer.introdue("Fred"))
# print(introducer.hello("Fred", "Sonali"))

#Create a class called Reminder. It should work like this:
class Reminder:
  def __init__(self, name):
    self.name = name

  def remind(self):
    return f'{self.name}! {self.walk}!'
  
  def remind_me_to(self, walk):
    self.walk = walk
    

reminder = Reminder("Sapna")
reminder.remind_me_to("Walk the dog")
print(reminder.remind())
