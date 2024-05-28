# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match (self,word_list):
        same_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) ==  self.word_letters:
                same_word_list.append(word)
        return same_word_list



    