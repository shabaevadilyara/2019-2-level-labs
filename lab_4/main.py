import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    if texts is None:
        return []
    if not isinstance(texts, list):
        return []

    text = []

    for sentence in texts:
        if isinstance(sentence, str) and sentence is not None:
            sentences = ''
            while '<br />' in sentence:
                sentence = sentence.replace('<br />', ' ')
            for sym in sentence:
                if sym.isalpha() or sym == ' ':
                    sym = sym.lower()
                    sentences += sym
            text.append(sentences.split(' '))
    for sentence in text:
        if '' in sentence:
            sentence.remove('')
    return text


texts = ['This is an example of test text. It contains two sentences.', 'Das ist ein Testtext. Es ist auf deutsch geschrieben.']


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if not self.corpus:
            return []
        for sentence in self.corpus:
            if not sentence:
                continue
            length = len(sentence)
            tf_values = {}
            frequencies = {}
            for word in sentence:
                if not isinstance(word, str):
                    length -= 1
            for word in sentence:
                if isinstance(word, str):
                    if word not in frequencies:
                        frequencies[word] = 1
                    else:
                        frequencies[word] += 1
            for word in frequencies:
                tf_values[word] = frequencies[word]/length
            self.tf_values.append(tf_values)
        return self.tf_values

    def calculate_idf(self):
        if not self.corpus:
            return {}
        for sentence in self.corpus:
            if not sentence:
                continue
            new_sentence = []
            idf = {}
            for word in sentence:
                if isinstance(word, str):
                    if word not in new_sentence:
                        new_sentence.append(word)
                for word in new_sentence:
                    k = 0
                    for i in self.corpus:
                        if not i or word in i:
                            k += 1
                    idf[word] = k
            for word in idf:
                self.idf_values[word] = math.log(len(self.corpus)/idf[word])
        return self.idf_values

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return []
        for i in self.tf_values:
            tf_idf_values = {}
            for k, v in i.items():
                tf_idf_values[k] = v * self.idf_values[k]
            self.tf_idf_values.append(tf_idf_values)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        dict_c = self.tf_idf_values[document_index]
        if word not in dict_c:
            return ()
        list_keys = sorted(dict_c, key = dict_c.__getitem__, reverse=True)
        return (dict_c[word], list_keys.index(word))


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
