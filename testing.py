import phoneme_dictionaries

words_to_phonemes = phoneme_dictionaries.get_word_to_phonemes_dict()

word_length = []
n_phonemes = []

for word in words_to_phonemes:
    for phonemes in words_to_phonemes[word]:
        word_length.append(len(word))
        n_phonemes.append(len(phonemes))

from matplotlib import pyplot as plt
import numpy as np

covariance_mat = np.cov(word_length, n_phonemes)
slope = covariance_mat[0][1] / covariance_mat[0][0]
intercept = np.mean(n_phonemes) - slope * np.mean(word_length)
word_range = list(range(max(word_length) + 2))

plt.plot(word_length, n_phonemes, '.')
plt.plot(word_range, [slope * i + intercept for i in word_range])
plt.title('y = {} * x + {}'.format(slope, intercept))
plt.show()

print(end='')
