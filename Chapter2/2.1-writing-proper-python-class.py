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
  
dog1 = Dog("Buddy", 3)
dog2 = Beagle("Maxy", 2)

# Cup class can hold multiple Dog objects
class DogCup:
  """
    A class to represent a cup that holds multiple dogs

    Attributes:
        dogs (list): A list of Dog objects in the cup
    """
  
  def __init__(self):
    self.dogs = [] # initialize empty list to hold dogs
    
  def __str__(self):
    # return f'The number of dogs in the DogCup: {len(self.dogs)}'
    return f"DogBasket with {len(self.dogs)} dogs."
    
  def add_dog(self, dog):
    """Add a Dog object to the cup"""
    self.dogs.append(dog)
  
  def __str__(self):
    return f'{self.dogs}'
  
  def __len__(self):
    return len(self.dogs)
  
  def __getitem__(self, index):
    return self.dogs[index]
    
    
# Example usage of the Cup class / # stringify changes output
my_cup = DogCup()
print(my_cup)

# Adding a dog object
my_cup.add_dog(dog1)
# print(my_cup)

# Adding a dog object from beagle
my_cup.add_dog(dog2)
# print(my_cup)

# calling __len__ object
# print(len(my_cup))

# get item or specific dog
# print(my_cup[0])

# output the stringified version of cup
print(my_cup)