from sys import stderr
import phoneme_dictionaries


class Instance:
    def __init__(self, instance):
        self.input = instance.strip()
        self.words = None
        self.phonemes = None
        self.composite_dict = {}
        self.piecewise_solutions = None
        self.solutions = None

    def get_words(self):
        if self.words is None:
            self.words = self.input.split()
        return self.words

    def get_phonemes(self):
        if self.phonemes is None:
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
            self.phonemes = phonemes
        return self.phonemes

    def get_solution(self, phonemes):
        if phonemes not in self.composite_dict:
            solution = []
            phonemes_to_word = phoneme_dictionaries.get_phonemes_to_word_dict()
            # phonemes are in the regular dictionary
            solution.extend(phonemes_to_word.get(phonemes, []))
            # phonemes are two solutions concatenated:
            for k in range(1, len(phonemes)):
                first = self.get_solution(phonemes[:k])
                second = self.get_solution(phonemes[k:])
                for f in first:
                    for s in second:
                        sol = f + ' ' + s
                        if sol not in solution:
                            solution.append(sol)
            self.composite_dict[phonemes] = solution
        return self.composite_dict[phonemes]

    def get_piecewise_solutions(self):
        if self.piecewise_solutions is None:
            piece_sol_list = []
            for part in self.get_phonemes():
                if isinstance(part, list):
                    piece_sol_list.append([])
                    for phonemes in part:
                        piece_sol_list[-1].extend(self.get_solution(phonemes))
                else:  # str
                    piece_sol_list.append([part])
            self.piecewise_solutions = piece_sol_list
        return self.piecewise_solutions

    def get_all_solutions(self):
        if self.solutions is None:
            partial_solutions = self.get_piecewise_solutions().copy()  # copy
            while len(partial_solutions) > 1:
                first, second = partial_solutions[-2:]
                if isinstance(first, str):
                    first = [first]
                if isinstance(second, str):
                    second = [second]
                result = []
                for f in first:
                    for s in second:
                        result.append(f + ' ' + s)
                partial_solutions = partial_solutions[:-2] + [result]
            self.solutions = partial_solutions[0]
        return self.solutions


if __name__ == '__main__':
    a = 'hello'
    ai = Instance(a)
    # ar = ai.get_solution()
    # print(ar)
    print(end='')
