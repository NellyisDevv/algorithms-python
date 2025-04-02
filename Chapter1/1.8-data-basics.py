# 1.8.1. Built-in Atomic Data Types¶

'''
print(2+3*4) 
print((2+3)*4) 
print(2**10) # exponentiation
print(6/3) # division
print(7/3) # division
print(7//3) # integer division
print(7%3) # remainder
print(3/6) # division
print(3//6) # integer division
print(3%6) # remainder
'''


'''
print(2 > 3)
print (2 < 3)
print (2 >= 2)
print (2 == 5)
print (2 != 5)
print (2 and 3) # always prints 3
print (2 or 8) # always prints 2
'''


# 1.8.2 Built-in Collection Data Types

myList = [1, 3, True, 6.5]
print(myList)
myList.append(4)
print(myList)
print(myList.pop())
print(myList)
A = myList
B = myList
myList = [0] * 6
print(myList)
print(A)
A[2] = 45
print(A)

# indexing

listOne = [2, 3, True, 7.7]
listTwo = [1, 4, False, 1.7]

# concatenation

listThree = listOne + listTwo
print(listThree)

# repetition

listThree = listThree * 3
print(listThree)

# membership

item = 2

if item in listOne:
  print (f"{item} is in listOne")
  
if item in listTwo:
  print (f"{item} is in listTwo")
else:
  print (f"{item} is not in listTwo")
  
# length

listOneLegnth = len(listOne)
print (f"The length of list one is {listOneLegnth}")

# slicing

listNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listNumbersSliced = listNumbers[1:6]
print (f"Sliced List {listNumbersSliced}")

# practice

"""
1. Create two indexs
2. Concatenate them together
3. Find an item inside of the concatenated index (membership)
4. Slice the item out of the concatenated index
5. Try to find the item inside of that index again (if else)
"""

# Solution

indexOne = [1, 2, True, 3.8]
indexTwo = [3, 8, False, 1.1]

indexThree = indexOne + indexTwo
print (f"indexThree: {indexThree}")

item  = 1

if item in indexThree:
  print (f"{item} IS in indexThree")
else:
  print (f"{item} is NOT in indexThree")
  
indexThreeSliced = indexThree[2:8]
print (f"indexThree Sliced: {indexThreeSliced}")

# item methods

babyNames = ['Noah', 'Paul', 'Jacob', 'Matthew']

babyNames.append('Jake')
print(f"{babyNames}")

babyNames.insert(0, 'Rebeka')
print(f"{babyNames}")

babyNames.pop()
print(f"{babyNames}")

babyNames.pop(0)
print(f"{babyNames}")

babyNames.sort()
print(f"{babyNames}")

babyNames.reverse()
print(f"{babyNames}")

# print(babyNames.index("Jake"))
print(babyNames.index("Matthew"))

print(babyNames.count("Matthew"))

babyNames.remove("Matthew")
print(f"{babyNames}")

print((54).__add__(21))

print(range(0, 10))

for i in range(3):
  print (f"Range of 3: {i}")
  
for i in range(1, 5):
  print (f"Range between 1 & 5: {i}")
  
for i in range (1, 5, 2):
  print (f"Range between 1 & 5 but step up by 2s: {i}")
  
# list()
  
print(list(range(10)))

# strings

myName = 'Nelly'
print(myName)
firstLetter = myName[0]
print(f"The first letter of my name is {firstLetter}")
myNameTimesThree = myName*3
print(len(myNameTimesThree))

# find

print(myName.upper())
print(myName.center(10))
print(myName.find('N')) # 0 = first letter of string
print(myName.split('l')) # two "l's" will split out both

# myName[0]='X' # not allowed strings can't be mutated

# tuple

myTuple = (2, True, 4.96) # like lists but similar to strings in they can't be mutated

# sets

# dont allow duplicates

mySet = {3, 6, "cat", 4.5, False}
invalidSet = {3, 3, 3, 6, "cat", "dog", True}
print(invalidSet) # other 3's are taken out of print statement

print(False in mySet)
print("bird" in invalidSet)

# methods provided by sets

print(mySet.union(invalidSet)) # returns all values from both sets (not duplicates)
print(mySet.intersection(invalidSet)) # returns values only in both sets
mySet.add(23) # adds item to set
print(mySet)
mySet.remove(23) # removes 23 from set
print(mySet)
mySet.pop() # removes arbitrary element from the set
print(mySet)
# mySet.clear() # removes all elements from set

# dictionary (key / values)

bestCities = {'Florida' : 'Tampa', 'Georgia' : 'Atlanta'}
print(bestCities)
print(bestCities['Florida'])
bestCities['Florida'] = 'St Pete'
print(bestCities['Florida'])

# operators provided by dictionary

print(bestCities.keys())
print(bestCities.values())
bestCitiesKeyList = list(bestCities.keys())
print(f"Here is the list of the best cities {bestCitiesKeyList}")
print(bestCities.items())
print(bestCities.get('Florida'))

