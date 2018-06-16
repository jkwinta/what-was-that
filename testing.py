from get_phoneme_dictionary import get_phoneme_dictionary

words_to_phoneme = get_phoneme_dictionary()

for w in words_to_phoneme:
    if not w[0].isalpha():
        print(w)

print(end='')
