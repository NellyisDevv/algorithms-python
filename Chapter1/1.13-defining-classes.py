# defining classes

# dog class

# __init__: initializes objects values
# def bark(slef): method (function) returns string
# __str__: method that returns object values as string instead of an object

class Dog:
  """
  A class to represent a dog.
  
   name (str): The name of the dog.
    age (int): The age of the dog in years.
  """
  def __init__(self, name, age):
    self.name = name # attribute for dogs name
    self.age = age # attribute for dogs age

  def bark(self):
    return f'{self.name} says woof!' # method that makes dog bark
  
  # comment out code below and you get an object returned when class is called
  # <__main__.Dog object at 0x100d41a90>
  def __str__(self):
    return f'Name: {self.name}, Age: {self.age}' # string representation of the Dog object
  
  # method to combine two dogs
  def __add__(self, other):
    return Dog('Combined Dog', self.age + other.age) # combine ages / # other is another object think: dog2
  
    # self is the dog in this object itself
  def __repr__(self):
    return f"Dog(name = '{self.name}', age= {self.age})" # offical string representation of the Dog object
  
  def __eq__(self, other):
    return self.age == other.age # check if dog ages are equal
  
  def __lt__(self, other):
    return self.age < other.age # check if one dog is younger
    

  
# subclass of dog
class Beagle(Dog):
  def bark(self):
    return f'{self.name} says arf!'  # corrected line
  
# output of __add__ method
dog1 = Dog('Buddy', 3)
dog2 = Dog('Maxy', 2)
combined_dog = dog1 + dog2 # uses the __add__ method
print(combined_dog.age)

# output of check if equal method __eq__ 
print(dog1 == dog2)

# output of check if greater than method __lt__
print(dog1 > dog2)


# output of string representation or __repr__
print(repr(dog1))

# output of dog object / __str__ will make it a string representation if active
# if __str__ active output equals: Output: Dog(Name: Buddy, Age: 3)
stray_dog = Dog('unknown', 3)
print(stray_dog)

# outout of bark method 
my_dog = Dog('Rover', 8)
print(my_dog.bark())

# output of beagle child class
my_beagle = Beagle('Max', 2)
print(my_beagle.bark())

class Cup:
  """
    A class to represent a cup that holds multiple dogs

    Attributes:
        dogs (list): A list of Dog objects in the cup
    """
  
  def __init__(self):
    self.dogs = [] # initialize empty list to hold dogs
    
  def add_dog(self, dog):
    """Add a Dog object to the cup"""
    self.dogs.append(dog)
    
    
# Example usage of the Cup class
my_cup = Cup()
print(my_cup)