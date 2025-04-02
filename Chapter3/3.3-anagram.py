# anagram detection example

def are_anagrams(word1, word2):
  # Sort the letters of both words and compare
  return sorted(word1) == sorted(word2)

# print(sorted('Hello'))
# print(sorted('zabc')) # notice on print z is last because sorted sorts alphabetically
anagram1 = are_anagrams('listen', 'silent')
# print(anagram1)
anagram2 = are_anagrams('dog', 'god')
# print(anagram2)
anagram3 = are_anagrams('hello', 'world')
# print(anagram3)

def count_letters(word):
  # Create a dictionary to count letters
  letter_count = {}
  for letter in word:
    if letter in letter_count:
      letter_count[letter] += 1 # Increment count if letter exists
    else:
      letter_count[letter] = 1 # Initialize count if letter is new
  return letter_count

def are_anagrams(word1, word2):
  # Count letters in both words and compare
  return count_letters(word1) == count_letters(word2)

print(count_letters('dog'))
print(count_letters('dog'))
anagram4 = are_anagrams('dog', 'god')
print(anagram4)
  