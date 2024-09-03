class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = file.read().split()
                index = -1
                for j in words:
                    index += 1
                    if j in ',.=!?;:-':
                        words.remove(j)
                    elif j[-1] in ',.=!?;:-':
                        words[index] = j[:-1].lower()
                    else:
                        words[index] = j.lower()
                all_words[i] = words
                file.close()
        return all_words

    def find(self, word):
        find_words = {}
        for key, values in self.get_all_words().items():
            if word.lower() in values:
                find_words[key] = values.index(word.lower()) + 1
        return find_words

    def count(self, word):
        count_word = {}
        for key, values in self.get_all_words().items():
            count_word[key] = values.count(word.lower())
        return count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего