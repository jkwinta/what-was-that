from urllib import request
import os

DICTIONARY_FILE = 'cmudict-0.7b'
DICTIONARY_URL = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b'

PUNCTUATION_EXCEPTIONS = ('3D', "'TIL", "'TIS", "'TWAS", "'ROUND", "'S", "'KAY", "'M", "'N", "'FRISCO", "'GAIN",
                          "'BOUT", "'CAUSE", "'COURSE", "'CUSE", "'EM", "'ALLO")

WORD_TO_PHONEMES_DICT = None
PHONEMES_TO_WORD_DICT = None


def build_word_to_phonemes_dict():
    if not os.path.isfile('./' + DICTIONARY_FILE):
        print("Downloading dictionary...")
        req_response = request.urlopen(DICTIONARY_URL)
        phoneme_dict_str = req_response.read().decode('latin-1')
        write_dict = ''
        while write_dict.lower() not in ('y', 'n'):
            write_dict = input("Write phoneme dictionary to file for future you? [y/n] ").strip()
        if write_dict.lower() == 'y':
            with open('./' + DICTIONARY_FILE, 'w') as f:
                f.write(phoneme_dict_str)
    else:
        with open('./' + DICTIONARY_FILE) as f:
            phoneme_dict_str = f.read()
    global WORD_TO_PHONEMES_DICT
    WORD_TO_PHONEMES_DICT = {}
    for line in phoneme_dict_str.split('\n'):
        if line and not line.startswith(';;;'):
            line = line.split()
            word = line[0]
            # remove numbers indicating stress
            phonemes = tuple(''.join([c for c in ph if not c.isdigit()]) for ph in line[1:])
            if not word[0].isalpha() and word != '3D':
                # TODO: specific allowed bits, associated with advanced word splitting?
                pass
            elif word[-1] == ')' and word[-3] == '(':
                # TODO: alternate pronunciations
                pass
            else:
                WORD_TO_PHONEMES_DICT[word] = phonemes


def build_phonemes_to_word_dict():
    word_to_phonemes = get_word_to_phonemes_dict()
    global PHONEMES_TO_WORD_DICT
    PHONEMES_TO_WORD_DICT = {}
    for word, phonemes in word_to_phonemes.items():
        if phonemes not in PHONEMES_TO_WORD_DICT:
            PHONEMES_TO_WORD_DICT[phonemes] = [word]
        else:
            PHONEMES_TO_WORD_DICT[phonemes].append(word)


def get_word_to_phonemes_dict():
    if WORD_TO_PHONEMES_DICT is None:
        build_word_to_phonemes_dict()
    return WORD_TO_PHONEMES_DICT


def get_phonemes_to_word_dict():
    if PHONEMES_TO_WORD_DICT is None:
        build_phonemes_to_word_dict()
    return PHONEMES_TO_WORD_DICT
