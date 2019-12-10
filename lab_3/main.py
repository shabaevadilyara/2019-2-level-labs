"""
Labour work #3
 Building an own N-gram model
"""

import math

#REFERENCE_TEXT = ''
#if __name__ == '__main__':
    #with open('not_so_big_reference_text.txt', 'r') as f:
        #REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if type(word) is str and word is not None:
            if word not in self.storage:
                self.storage[word] = len(self.storage)
        else:
            return {}
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if type(word) is str and word is not None:
            if word not in self.storage:
                return -1
            else:
                return self.storage[word]
        return -1

    def get_original_by(self, id: int) -> str:
        for key, value in self.storage.items():
            if type(id) is int and id is not None:
                if id != value:
                    return 'UNK'
                else:
                    return key
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if corpus is not None and type(corpus) is tuple:
            for sym in corpus:
                if type(sym) is str and sym is not None:
                    self.put(sym)
                else:
                    return {}
            return self.storage
        else:
            return {}


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.sentence_list_main = []

    def fill_from_sentence(self, sentence: tuple) -> str:
        for i in range(len(sentence) - self.size + 1):
            bigram = (sentence[i], sentence[i+1])
            if bigram not in self.gram_frequencies:
                self.gram_frequencies[bigram] = 1
            else:
                self.gram_frequencies[bigram] += 1
        print(self.gram_frequencies)
            
    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass

n = NGramTrie(2)
n.fill_from_sentence((1, 2, 3, 4, 5))

def encode(storage_instance, corpus) -> list:
    encoded_corpus = []
    new_corpus = []
    if corpus is not None:
        for sym in corpus:
            for word in sym:
                storage_instance.get_id_of(word)
                encoded_corpus.append(storage_instance.get_id_of(word))
            new_corpus += encoded_corpus
    else:
        return []
    return encoded_corpus


def split_by_sentence(text: str) -> list:
    if not text or ' ' not in text:
        return []
    text += ' A'
    new_text = ''
    new_new_text = []
    for symbol in text:
        if symbol.isalpha() or symbol == ' ' or symbol in '.!?':
            if symbol in '!?':
                new_text += '.'
            else:
                new_text += symbol
    k = 0
    for i in range(len(new_text) - 2):
        if new_text[i] == '.' and new_text[i + 1] == ' ' and new_text[i + 2] in " QWERTYUIOPLKJHGFDSAZXCVBNM":
            new_new_text.append(new_text[k: i])
            k = i + 2
    new_sentence = []
    for i in new_new_text:
        phrase1 = i.split(' ')
        phrase = [symbol.lower() for symbol in phrase1 if symbol != '']
        phrase = ['<s>'] + phrase + ['</s>']
        new_sentence.append(phrase)
    print(new_sentence)
    return new_sentence


text = "Mar#y wa$nted, to swim! However, she was afraid of sharks."
storage_instance = WordStorage()
split_by_sentence(text)
corpus = split_by_sentence(text)
for sentence in corpus:
    storage_instance.from_corpus(tuple(sentence))
encode(storage_instance, corpus)
