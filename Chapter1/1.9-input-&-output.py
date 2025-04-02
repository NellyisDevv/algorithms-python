# input and output

'''
aName = input('please enter a name')
print(f"Welcome, {aName}! Your name in all captials is {aName.upper()}")
print(f"The length of your name is: {len(aName)}")
'''

# switch value type

'''
sradius = input('Please enter the radius of the circle')
radius = float(sradius)
diameter = 2 * radius
print(diameter)
'''

# string formatting

print('Hello')
print('Hello','World')
print('Hello','World', sep='***') # Hello***World
print('Hello', 'World', end='***') # Hello World***

# formatted strings

name = 'Nelly'
age = 23
print(name, 'is', age, 'years old.')
print("%s is %d years old." % (name, age)) # %s = string / %d = number
# % = format operator / left side = template format / right = collection of values corresponds with num of %
'''
# %d or i = integer
# %u = unsigned integer
# %f = floating point as m.ddddd
'''

# format modifier
'''
# %20d = put the value in a field width of 20
%-20d = put the value in a field 20 characters wide, left-justified
%20.2f = put the value in a field 20 characters wide with 2 characters to the right of the decimal point.
%(name)d = get the value from the supplied dictionary using name as the key.
'''
price = 24
item = 'banana'
print('The %s costs %d cents' % (item, price))
print('The %+10s costs %5.2f cents' % (item, price))

item_info = {'name': 'apple', 'price': 50}
print('The %(name)s costs %(price)d cents' % item_info)