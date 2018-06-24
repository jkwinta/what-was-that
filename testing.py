from get_phoneme_dictionary import get_phoneme_dictionary

words_to_phoneme = get_phoneme_dictionary()

# for w in words_to_phoneme:
#     if not w[0].isalpha():
#         print(w)

a = []
for w in words_to_phoneme:
    if '(' in w and ')' in w and ')' != w[-1] and '(' != w[-3]:
        a.append(w)

print(end='')
