from sys import stderr


class Instance:
    def __init__(self, instance):
        self.input = instance
        # self.words = instance.split()
        self.words = None
        self.phonemes = None
        # self.next = None
        self.array = None
        self.solution = None

    def get_words(self):
        if self.words is None:
            try:
                self.words = self.input.split()
            except AttributeError:
                print("Invalid input", file=stderr)
        return self.words

    def get_phonemes(self):
        pass

    def get_solution(self):
        if self.solution is None:
            self.compute_solution()
        return self.solution

    def compute_solution(self):
        pass
