#Find the first reoccuring letter from a given string of letters

def recuring_letter(strings):
  counts = {}
  for letter in strings:
    if letter in counts:
      return letter
    counts[letter] = 1
  return None

recuring_letter("bcaba")