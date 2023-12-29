# your code goes here!

class Anagram:

  def __init__(self, word):
    self.word = word

  def match(self, word_list):
    anagrams = []

    letters_in_word = [letter for letter in self.word]

    for element in word_list:
      letters_in_list = [letter for letter in element]
      if sorted(letters_in_list) == sorted(letters_in_word):
        anagrams.append(element)
        #print(anagrams)
        
    return anagrams

listen = Anagram("enlist")
listen.match(["listen", "silent", "hippopotamus"])
