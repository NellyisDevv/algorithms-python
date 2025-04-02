# 3.7 dict

my_dict = {
  'name': 'alice',
  'age': 30,
}

another_dict = dict(name='Bob', age=25, city='Tampa')

name = another_dict['name'] # Returns Bob

print(name)

another_dict['name'] = 'Bill'  # Change the value associated with the key 'name'
# value needs to be reassinged before update can be referenced again
name = another_dict['name']  # Update the variable 'name' to reflect the new value
print(name)

print(another_dict['city'])
another_dict.pop('city')
print(another_dict)

for key in my_dict:
  print(key, my_dict[key])
  
for value in my_dict:
  print(my_dict[value])
  
for key, value in my_dict.items():
    print(key, value) 
    
# Retrieving a value by its key is O(1)
# Inserting a Key-Value Pair: Adding a new key-value pair is also O(1) on average.
# Removing a Key-Value Pair: Deleting a key-value pair is O(1) on average.

# The space complexity of a dictionary is O(n), where n is the number of key-value pairs. This is because each entry requires space to store both the key and the value.