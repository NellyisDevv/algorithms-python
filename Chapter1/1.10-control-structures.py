# control structures

# while (executes over a block of code)
# loops while a condition is met

counter = 1
while counter <= 5:
  print ('Hello, World!')
  counter += 1
  
# for (iterates over a sequence i.e. lists, tuples, or strings)
# iterates until sequence is complete
'''
for item in [1, 3, 6, 2, 5]:
  print(item)
'''

  
# iterate over a range of numbers

for item in range(5):
  print(item*2)
  
# iterate over characters in strings or lists

'''
cities = ['tampa', 'st pete', 'miami', 'naples']
letterlist = []
for city in cities:
  print(city)
  for aword in cities:
    for aletter in aword:
      letterlist.append(aletter)
  print(letterlist)
'''
  
# if else statements

n = 223
if n < 0:
  print(f'Your value {n}: is negative')
else:
  print(f'Your Vale {n}: is positive')

m = 20
if m < 0:
    print(f'Your value {m}: is negative')
else:
  if m < 5:
    print(f'Your value is less than 5')
  else:
    if m > 10:
      print(f'Your value is greater than 10')
    else:
      if m > 20:
        print(f'Your value is greater than 20')
        
# if else statements made easier
        
score = 49
if score >= 90:
  print('A')
elif score >= 80:
  print('B')
elif score >= 70:
  print('C')
elif score >= 60:
  print('D')
else:
  print('F')
  
if score < 100:
  score = abs(2)
  print(score)
  
# list comprehensions

sqlist = [x*x for x in range(1, 11)]
print(sqlist)

# add conditions to filter items

sqlistt = [x*x for x in range(1, 11) if x % 2 != 0]
print(sqlistt)

oddchecker = 2 % 3
if oddchecker is 0:
  print('Even Number!')
else:
  print('Odd Number!')
  
