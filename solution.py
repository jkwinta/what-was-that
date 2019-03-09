from sys import stderr
import phoneme_dictionaries


class Instance:
    def __init__(self, instance):
        self.input = instance.strip()
        self.words = None

    def get_words(self):
        if self.words is None:
            self.words = self.input.split()
        return self.words

    def get_phonemes(self):
        phonemes = []
        d = phoneme_dictionaries.get_word_to_phonemes_dict()
        for word in self.get_words():
            word_upper = word.upper()
            if word_upper in d:
                if not phonemes or not isinstance(phonemes[-1], list):
                    phonemes.append(d[word_upper])
                else:
                    last_phonemes = phonemes[-1]
                    phonemes[-1] = []
                    for first in last_phonemes:
                        for second in d[word_upper]:
                            phonemes[-1].append(first + second)
            else:
                phonemes.append(word)
        return phonemes


class SubInstance:
    def __init__(self, instance):
        self.input = instance.strip()
        self.words = None
        self.phonemes = None
        self.n_phonemes = 0
        # self.next = None
        self.array = {}

    def get_words(self):
        if self.words is None:
            self.words = self.input.split()
        return self.words

    def get_phonemes(self):
        if self.phonemes is None:
            phonemes_list = []
            d = phoneme_dictionaries.get_word_to_phonemes_dict()
            words = self.get_words()
            for word in words:
                word_upper = word.upper()
                if word_upper in d:
                    phonemes_list.extend(d[word_upper])
                else:
                    print('Word "{}" not in dictionary, result will be nonsense!'.format(word), file=stderr)
            self.phonemes = tuple(phonemes_list)
            self.n_phonemes = len(self.phonemes)
        return self.phonemes

    def get_result_by_range(self, start, stop):
        k = (start, stop)
        if self.array.get(k, None) is None:
            result = []
            result.extend(
                phoneme_dictionaries.get_phonemes_to_word_dict().get(self.get_phonemes()[start:stop], [])
            )
            for k in range(start + 1, stop):
                first = self.get_result_by_range(start, k)
                second = self.get_result_by_range(k, stop)
                for f in first:
                    for s in second:
                        c = f + ' ' + s
                        if c not in result:
                            result.append(c)
            self.array[k] = result
        return self.array[k]

    def get_solution(self):
        self.get_phonemes()
        return self.get_result_by_range(0, self.n_phonemes)


def get_solution(string_of_words):
    i = Instance(string_of_words)
    return i.get_solution()


if __name__ == '__main__':
    a = 'hello'
    ai = Instance(a)
    # ar = ai.get_solution()
    # print(ar)
    print(end='')
