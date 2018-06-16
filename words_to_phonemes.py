from get_phoneme_dictionary import get_phoneme_dictionary


def words_to_phonemes(words):
    word_to_phoneme_dict = get_phoneme_dictionary()
    result = []
    for word in words.split():
        result.extend(word_to_phoneme_dict.get(word.upper(), [-1]))
    return result
