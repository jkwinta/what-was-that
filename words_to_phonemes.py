from phoneme_dictionaries import get_phoneme_dictionary

WORD_TO_PHONEME_DICT = None


def words_to_phonemes(words):
    global WORD_TO_PHONEME_DICT
    if WORD_TO_PHONEME_DICT is None:
        WORD_TO_PHONEME_DICT = get_phoneme_dictionary()
    result = []
    for word in words.split():
        result.extend(WORD_TO_PHONEME_DICT.get(word.upper(), [-1]))
    return result
