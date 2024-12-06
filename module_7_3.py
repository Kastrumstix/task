import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words.extend(word for word in line.split() if word)
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word_positions = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                word_positions[name] = words.index(word.lower()) + 1
        return word_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            word_counts[name] = words.count(word.lower())
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))