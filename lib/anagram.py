class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, possible_words):
        matches = []
        for word in possible_words:
            if sorted(word.lower()) == self.sorted_word and word.lower() != self.word:
                matches.append(word)
        return matches
